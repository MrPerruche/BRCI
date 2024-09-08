import os
import shutil
from typing import TypeVar

from .brick import *
from .utils import *
from .write_utils import *
from .write_utils import _convert_brick_types
# import os.path -> from .utils
# from typing import Self -> from .brick
# from typing import Final -> from .utils

VISIBILITY_PUBLIC: Final[int] = 0
VISIBILITY_FRIENDS: Final[int] = 1
VISIBILITY_PRIVATE: Final[int] = 2
VISIBILITY_HIDDEN: Final[int] = 3

_VALID_DRIVER_SEATS: Final[set[str]] = {'Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'}


class Creation14:

    def __init__(self, project_name: str, project_dir: str,
                 name: str = '', description: str = '', appendix: bytes | bytearray = bytearray(), tags: list[str] | None = None,
                 visibility: int = VISIBILITY_PUBLIC, seat: Optional[str | int] = None, creation_time: Optional[int] = None,
                 update_time: Optional[int] = None) -> None:

        """
        Project creation class for version 14 (Brick Rigs 1.7.0+).

        :param project_name: Name of the folder in which all Brick Rigs file (Vehicle.brv etc.) will be stored.
        :param project_dir: Directory where these folders will go in.
        :param name: Name of the project displayed in-game.
        :param description: Description of the project displayed in-game.
        :param appendix: Hidden binary data in files.
        :param tags: List of tags for the project.
        :param visibility: Visibility of the project, set to VISIBILITY_PUBLIC, VISIBILITY_FRIENDS, VISIBILITY_PRIVATE or VISIBILITY_HIDDEN.
        :param seat: Name of the driver seat (if there is one).
        :param creation_time: Time the project was created (in 100s of nanoseconds since 0001-01-01 00:00:00 UTC).
        :param update_time: Time the project was last updated (in 100s of nanoseconds since 0001-01-01 00:00:00 UTC).
        """

        # Path related
        self.project_name: str = project_name
        self.project_dir: str = project_dir

        # Display text
        self.name: str = name
        self.description: str = description
        self.tags: list[str] = tags
        self.creation_time: Optional[int] = creation_time
        self.update_time: Optional[int] = update_time

        # File
        self.seat: Optional[str | int] = seat
        self.appendix: bytes | bytearray = appendix

        # Other
        self.visibility: int = visibility

        self.bricks: list[Brick14] = []

        # Private
        self.__FILE_VERSION: Final[int] = 14


    def add_brick(self,
                  brick_type: str,
                  name: str | int,
                  position: Optional[list[float]] = None,
                  rotation: Optional[list[float]] = None,
                  properties: Optional[dict[str, Any]] = None) -> Self:

        """
        Will add a new brick to the creation.

        :param brick_type:
        :param name:
        :param position:
        :param rotation:
        :param properties:
        :return:
        """

        self.bricks.append(self.Brick(brick_type, name, position, rotation, properties))

        return self


    def assert_valid_parameters(self, *args: str) -> None:

        # Project name
        if 'project_name' in args:

            # Valid folder name? cannot be mitigated.
            if not is_valid_folder_name(self.project_name, os.name == 'nt'):

                # Signal there's something wrong
                FM.error("Invalid project name.", "Your os do not support such folder names. As such, this project cannot be created.")

                raise OSError(f"Invalid project name: couldn't create a file named {self.project_name}." +
                              (" Error mitigation failed." if settings['attempt_error_mitigation'] else ""))

        # Project dir
        if 'project_dir' in args:

            # Valid project path? cannot be mitigated.
            if not os.path.exists(self.project_dir):

                # Signal there's something wrong
                FM.error("Invalid project path.", "The path you provided is not valid. As such, this project cannot be created.")

                raise OSError(f"Invalid project path: couldn't create a folder at {self.project_dir}." +
                              (" Error mitigation failed." if settings['attempt_error_mitigation'] else ""))


    def backup(self, dst: str = BACKUP_FOLDER, name: Optional[str] = None) -> Self:

        """
        Backup Brick Rigs' vehicle folder.

        :param dst: Directory where the backup will be stored.
        :param name: Name of the folder in which all Brick Rigs file (Vehicle.brv etc.) will be stored. If none, 100s of nanoseconds since 0001-01-01 00:00:00 UTC will be used.

        :return: self
        """

        # TODO: CHECK IF THIS IS VALID FOR POSIX SYSTEMS.

        folder_name = str(get_time_100ns()) if name is None else name

        # Assert everything is valid
        self.assert_valid_parameters('project_name', 'project_dir')

        if not os.path.exists(dst):

            FM.error("Backup folder not found.",
                     "The path you provided is missing or not valid. As such, this project cannot be created.")

            # This error is cannot be mitigated.
            raise OSError(f"Backup folder not found: couldn't create a folder at {dst}." +
                          (" Error mitigation failed." if settings['attempt_error_mitigation'] else ""))

        # See if there's a path that exist among the list of possible paths, if so, copy it to the backup folder
        try:
            for potential_src in BRICK_RIGS_FOLDER:
                if os.path.exists(potential_src):
                    shutil.copytree(potential_src, os.path.join(dst, folder_name))
                    return self
        # In case something went wrong, just indicating it was an issue whilst doing the backup.
        except OSError as e:
            raise OSError(f'Backup failed! ({e})')

        # Else, then it failed, so we end with an error.
        raise FileNotFoundError("No Brick Rigs vehicle folder found.")


    # Following class naming conventions instead.
    # noinspection PyPep8Naming
    @staticmethod
    def Brick(brick_type: str,
              name: str | int,
              position: Optional[list[float]] = None,
              rotation: Optional[list[float]] = None,
              properties: Optional[dict[str, Any]] = None) -> Brick14:

        """
        Will return the brick class used for this creation class.

        :param brick_type: Type of the brick.
        :param name: Name or identifier of the brick.
        :param position: (x, y, z) coordinates of the brick's position.
        :param rotation: (pitch, yaw, roll) angles in degrees for the brick's rotation.
        :param properties: Additional properties of the brick as key-value pairs.

        :return: Corresponding Brick14 object.
        """

        return Brick14(brick_type, name, position, rotation, properties)


    def get_version(self) -> int:
        return self.__FILE_VERSION


    def write_creation(self, file_name: str = 'Vehicle.brv', exist_ok: bool = True) -> Self:

        """
        Will write the .brv (vehicle) file

        :param file_name: Name of the file (Brick Rigs will search for Vehicle.brv)
        :param exist_ok: If Vehicle.brv already exists: if set to True, replace, else raise an error.
        :return: self
        """

        # #################### TREATMENT ####################

        # Bricks
        num_bricks: int = len(self.bricks)
        # Brick Types
        brick_types: set[str] = {brick.get_type() for brick in self.bricks}
        num_brick_types: int = len(brick_types)

        # Properties
        # Initialize variables
        # property_types: set[str] = set()  # Every single different property
        property_id_types: dict[int, str] = {}  # Property and their id
        property_types_id: dict[str, int] = {}  # Property id and their property
        property_id_values_set: dict[int, set[Any]] = {}  # Property id and their values

        for brick in self.bricks:
            for property_, value in brick.properties.items():

                # Adding to list of known properties
                # is None if missing else id (int)
                property_id = property_types_id.get(property_)

                if property_id is None:
                    property_id = len(property_types_id)
                    property_id_types[property_id] = property_
                    property_types_id[property_] = property_id
                    property_id_values_set[property_id] = set()
                property_id_values_set[property_id].add(value)
        # To avoid later issues or warnings, just in case
        del i




        # #################### WRITING ####################

        buffer: bytearray = bytearray()

        # -------------------- PART 1: HEADER --------------------

        # Version
        buffer.extend(unsigned_int(self.__FILE_VERSION, 1))

        # Bricks, unique bricks, unique properties
        buffer.extend(unsigned_int(num_bricks, 2))
        buffer.extend(unsigned_int(num_brick_types, 2))
        buffer.extend()

        # Brick types
        buffer.extend(_convert_brick_types(brick_types))










Creation = TypeVar('Creation', bound=Creation14)
