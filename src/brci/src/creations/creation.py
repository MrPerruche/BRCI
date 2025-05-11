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



    def get_full_path(self, name: Optional[str] = None) -> str:

        """
        Will return the path where all files will be written

        Arguments:
            name (Optional[str], optional): Pretend the name of this project is different.

        Returns:
            str: Path
        """

        return self.get_full_path_of(self.project_dir, self.project_name if name is None else name)



    @staticmethod
    def get_full_path_of(project_dir: str, project_name: str):

        """
        Will return the path where all files will be written

        Returns:
            str: Path
        """

        return os.path.join(project_dir, project_name)



    @staticmethod
    @abstractmethod
    def get_property_types_dict() -> dict[str, Type[BinaryType]]:
        pass



    @staticmethod
    @abstractmethod
    def Value():
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



    def apply(self, fn: Callable[[Brick], Brick | None]) -> Self:
        """
        Will apply a function to the creation's bricks, and replace the current brick with the return value, such as:

        Arguments:
            fn (Callable[[Brick], Brick | None]): Function to apply. May return None to make use of mutability or skip a brick.

        Returns:
            Self
        """

        for i, brick in enumerate(self.bricks):
            result = fn(brick)
            if result is not None:
                self.bricks[i] = result

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



    def copy(self):
        return deepcopy(self)



    @abstractmethod
    def deserialize_creation(self, file: bytearray) -> Self:
        pass



    @abstractmethod
    def merge(self, *args, **kwargs) -> Self:
        pass



    def move(self, x: int | float, y: int | float, z: int | float) -> Self:

        """
        Will move the creation's bricks.

        Arguments:
            x (int | float): X offset
            y (int | float): Y offset
            z (int | float): Z offset

        Returns:
            Self
        """

        for b in self.bricks:
            b.position = [x + b.position[0], y + b.position[1], z + b.position[2]]

        return self



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


    # FIXME this is basically just map() but returning self and not some weird map object
    def apply(self, fn: callable) -> Self:

        """
        Will apply a function to the creation's bricks, and replace the current brick with the return value.

        Arguments:
            fn (callable): Function to apply.

        Returns:
            Self
        """

        for i, brick in enumerate(self.bricks):
            self.bricks[i] = fn(brick)

        return self




creation_classes: dict[int, Type[Creation]] = {}


def register_creation(version: int, creation: Type[Creation]) -> None:
    creation_classes[version] = creation


def get_creation(version: int) -> Type | None:
    result = creation_classes.get(version)  # To get None
    if result is None:
        raise NotImplementedError(f"Creation version {version} is not supported")


def get_file_version(path: str) -> int:

    """
    Will return the file version of a Brick Rigs file.

    Arguments:
        path (str): Path to the creation file.

    Returns:
        int: File version
    """

    with open(path, 'rb') as f:
        return int(f.read()[0])


def get_creation_of(path: str) -> Type:

    """
    Will return the creation class of a Brick Rigs file.

    Arguments:
        path (str): Path to the creation file.

    Returns:
        Type: Sub-class of ModernCreation or LegacyCreation

    Exceptions:
        NotImplementedError: If the file version is not supported
    """

    result = get_creation(get_file_version(path))
    if result is None:
        raise NotImplementedError(f"Creation version {get_file_version(path)} is not supported")

    return result


def new_creation_from(project_name: str, project_dir: str, version_filter: Optional[Callable[[int], bool]] = None) -> Any:

    """
    Will create a new creation object of a file of an unknown version

    Arguments:
        project_name (str): Name of the project
        project_dir (str): Directory of the project
        version_filter (Optional[Callable[[int], bool]], optional): Function to filter the versions. Defaults to None. Raises error if returns false

    Returns:
        Any: Instance of a subclass of LegacyCreation or ModernCreation

    Exceptions:
        * Any exceptions that may arise from get_creation(...)
        NotImplementedError: If the file version is not supported
    """

    file_version = get_file_version(Creation.get_full_path_of(project_dir, project_name))

    if version_filter is not None and not version_filter(file_version):
        raise NotImplementedError(f"Creation version {file_version} is not supported")

    return get_creation(file_version)(project_name, project_dir)


def load_new_creation_from(project_name: str, project_dir: str, version_filter: Optional[Callable[[int], bool]] = None) -> Any:

    """
    Just like new_creation_from(...), it will create a new creation object of a file of an unknown version.
    .read_creation() will be called before returning the object.

    Arguments:
        project_name (str): Name of the project
        project_dir (str): Directory of the project
        version_filter (Optional[Callable[[int], bool]], optional): Function to filter the versions. Defaults to None. Raises error if returns false

    Returns:
        Any: Loaded instance of a subclass of LegacyCreation or ModernCreation

    Exceptions:
        * Any exceptions that may arise from get_creation(...)
        * Any exceptions that may arise from .read_creation()
        NotImplementedError: If the file version is not supported
    """

    creation = new_creation_from(project_name, project_dir, version_filter)
    creation.read_creation()
    return creation