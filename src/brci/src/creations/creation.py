from abc import ABC, abstractmethod
import os
from typing import Final, Self, Optional, Any, Callable, Type
from shutil import copytree as _shutil_copytree

from ..brick import *
from ..binary_types import BinaryType
from ..utils import *
from ..value_enums import Value


class Creation(ABC):


    # Method positions:

    # 1. Dunder methods (__init__ then alphabetical order)
    # 2. Getters / Setters (alphabetical order)
    # 3. Other (alphabetical order)


    def __init__(self, file_version: int, value_enums: Type[Value], project_name: str, project_dir: str) -> None:

        self.__FILE_VERSION: int = file_version
        self.Value = value_enums
        self.project_name: str = project_name
        self.project_dir: str = project_dir

        self.bricks: list = []



    def __repr__(self):
        attrs: str = ", ".join(f"{k}={v!r}" for k, v in self.__dict__.items())
        return f"{self.__class__.__name__}({attrs})"



    @classmethod
    @abstractmethod
    def get_brick_rigs_vehicle_folder(cls, potential_folders: Optional[list[str]] = None)  -> str:

        """
        Will return the path to the BrickRigs vehicle folder to be used as project_dir argument.

        Arguments:
            potential_folders (Optional[list[str]], optional): Override list of potential folders.

        Exceptions:
            FileNotFoundError: When BrickRigs folder is not found.

        Returns:
            str: Path
        """

        assert potential_folders is not None

        for path in potential_folders:
            if os.path.exists(path):
                return path

        raise FileNotFoundError("Unable to find a valid folder")



    def get_file_version(self) -> int:

        """
        Will return the file version of the creation instance

        Returns:
             int: Vehicle and metadata file version
        """

        return self.__FILE_VERSION



    def get_full_path(self) -> str:

        """
        Will return the path where all files will be written

        Returns:
            str: Path
        """

        return os.path.join(self.project_dir, self.project_name)



    @staticmethod
    @abstractmethod
    def get_property_types_dict() -> dict[str, Type[BinaryType]]:
        pass


    @staticmethod
    @abstractmethod
    def get_bricks_dict() -> dict[str, Brick]:
        pass



    def add_brick(self,
                  brick_type: str,
                  name: str | int,
                  position: Optional[list[float]] = None,
                  rotation: Optional[list[float]] = None,
                  properties: Optional[dict[str, Any]] = None) -> Self:

        """
        Will add a new brick to the creation.

        Arguments:
            brick_type (str): Type of the brick.
            name (str | int): Name or identifier of the brick.
            position (Optional[list[float]], optional): (x, y, z) coordinates of the brick's position. Defaults to None.
            rotation (Optional[list[float]], optional): (pitch, yaw, roll) angles in degrees for the brick's rotation. Defaults to None.
            properties (Optional[dict[str, Any]], optional): Additional properties of the brick as key-value pairs. Defaults to None.

        Exceptions:
            ValueError: If the brick type does not exist
            TypeError: One of the arguments is of invalid type
        """

        self.bricks.append(self.Brick(brick_type, name, position, rotation, properties))
        return self



    def backup(self, dst: str = BACKUP_FOLDER, name: Optional[str] = None) -> Self:

        """
        Backup Brick Rigs' vehicle folder.

        Arguments:
            dst (str, optional): Directory where the backup will be stored.
            name (Optional[str], optional): Name of the folder in which all Brick Rigs file (Vehicle.brv etc.) will be stored. If none, 100s of nanoseconds since 0001-01-01 00:00:00 UTC will be used.

        Exceptions:
            OSError: Project name (project_name) is invalid
            OSError: Project dir (project_dir) is invalid
            OSError: Backup folder (dst param) not found
            OSError: Backup failed
            FileNotFoundError: No Brick Rigs vehicle folder found.

        Returns the current object.
        """

        # TODO: CHECK IF THIS IS VALID FOR POSIX SYSTEMS.

        if os.name == 'posix':
            pass
            # ("warning",
            #         "Creation14::backup || This function is still a work in progress and may not work on POSIX systems.")

        folder_name = str(get_time_100ns()) if name is None else name

        # Assert everything is valid
        if not is_valid_folder_name(self.get_full_path(), os.name == 'nt'):
            raise OSError(f"Invalid project name: couldn't create a file named {self.project_name}.")

        if not os.path.exists(dst):
            raise OSError(f"Backup folder not found: couldn't create a folder at {dst}.")

        # See if there's a path that exist among the list of possible paths, if so, copy it to the backup folder
        try:
            for potential_src in self.get_brick_rigs_vehicle_folder():
                if os.path.exists(potential_src):
                    _shutil_copytree(potential_src, os.path.join(dst, folder_name))
                    return self
        # In case something went wrong, just indicating it was an issue whilst doing the backup.
        except OSError as e:
            # logwrap("critical", f"Creation14::backup || Backup failed! ({e})")
            raise OSError(f'Backup failed! ({e})') from e

        # Else, then it failed, so we end with an error.
        # logwrap("critical", f"Creation14::backup || No Brick Rigs vehicle folder found!")
        raise FileNotFoundError("No Brick Rigs vehicle folder found.")



    # noinspection PyPep8Naming
    @staticmethod
    @abstractmethod
    def Brick(brick_type: str,
              name: str | int,
              position: Optional[list[float]] = None,
              rotation: Optional[list[float]] = None,
              properties: Optional[dict[str, Any]] = None):

        """
        Will return the brick class used for this creation class.

        Arguments:
            brick_type (str): Type of the brick.
            name (str | int): Name or identifier of the brick.
            position (Optional[list[float]], optional): (x, y, z) coordinates of the brick's position. Defaults to None.
            rotation (Optional[list[float]], optional): (pitch, yaw, roll) angles in degrees for the brick's rotation. Defaults to None.
            properties (Optional[dict[str, Any]], optional): Additional properties of the brick as key-value pairs. Defaults to None.

        Returns:
            Brick<version>: Newly created Brick<version> object; e.g. Creation14.Brick -> Brick14

        Exceptions:
            ValueError: If the brick type does not exist
            TypeError: Name is of invalid type
        """

        pass


    @abstractmethod
    def deserialize_creation(self, file: bytearray) -> Self:
        pass



    def read_creation(self, file_name: str = 'Vehicle.brv'):

        """
        Will read the .brv (vehicle) file, and append it to the creation's bricks.

        Arguments:
            file_name (str, optional): Path of the .brv file

        Returns:
            Self

        Exceptions:
            FileNotFoundError: Invalid path
            NotImplementedError: The file being read is from a different version
        """

        read_path = os.path.join(self.get_full_path(), file_name)

        if not os.path.exists(read_path):
            raise FileNotFoundError(f"File {file_name} not found")

        with open(read_path, 'rb') as f:
            self.deserialize_creation(bytearray(f.read()))

        return self



    @abstractmethod
    def rename_bricks(self, *args, **kwargs):
        pass



    @abstractmethod
    def serialize_creation(self) -> bytearray:

        """
        Will generate the creation and return it as a bytearray

        Returns:
            bytearray: Creation file
        """

        pass



    def write_creation(self, file_name: str = 'Vehicle.brv', exist_ok: bool = True) -> Self:

        """
        Will generate and write the creation file

        Arguments:
            file_name (str, optional): Name of the file to write.
            exist_ok (bool, optional): If True, will overwrite the file if it already exists.

        Exceptions:
            * Exceptions from .serialize_creation()
            FileExistsError: File already exists and exist_ok is set to False

        Returns:
            Self
        """

        write_path: str = os.path.join(self.get_full_path(), file_name)

        if not exist_ok and os.path.exists(write_path):
            raise FileExistsError(f"Following file already exists: {write_path}")

        os.makedirs(self.get_full_path(), exist_ok=True)
        with open(write_path, 'wb') as f:
            f.write(self.serialize_creation())

        return self



    def write_preview(self, *args, **kwargs) -> Self:
        pass
