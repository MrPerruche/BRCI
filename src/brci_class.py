import os
import shutil

from .brick import *
from .brick import _Brick
from .utils import *
# import os.path -> from .utils
# from typing import Self -> from .brick
# from typing import Final -> from .utils

VISIBILITY_PUBLIC: Final[int] = 0
VISIBILITY_FRIENDS: Final[int] = 1
VISIBILITY_PRIVATE: Final[int] = 2
VISIBILITY_HIDDEN: Final[int] = 3

_VALID_DRIVER_SEATS: Final[set[str]] = {'Seat_2x2x7s', 'Seat_3x2x2', 'Seat_5x2x1s'}


# Default class for inheritance
class _Creation:

    def __init__(self, project_name: str, project_dir: str,
                 name: str = '', description: str = '', appendix: bytearray = bytearray(), tags: list[str] | None = None,
                 visibility: int = VISIBILITY_PUBLIC, seat: Optional[str | int] = None, creation_time: Optional[int] = None,
                 update_time: Optional[int] = None) -> None:

        """
        Internal class, blank project creation class.

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
        self.appendix: bytearray = appendix

        # Other
        self.visibility: int = visibility

        self.bricks: list[_Brick] = []

        # Private
        # self.__BRV_VERSION


    def assert_valid_parameters(self, *parameters: str) -> Self:

        """
        Assert that the parameters are valid.

        :param parameters: List of parameters to check. Include '*' to check all parameters.

        :return:
        """

        # Check all parameters
        check_all: bool = False
        if '*' in parameters:
            check_all = True

        # Make sure everything is set to the right values
        # self.project_name is invalid if it is not a valid folder name
        if check_all or 'project_name' in parameters:
            assert is_valid_folder_name(self.project_name, os.name == 'nt'), "Invalid project name. It must be a valid folder name."

        # self.project_dir is invalid if it doesn't exist
        if check_all or 'project_dir' in parameters:
            assert os.path.exists(self.project_dir), "Project folder directory not found."

        # self.name is invalid if it is not a string
        if check_all or 'name' in parameters:
            assert isinstance(self.name, str), "Display name must be a string."

        # self.description is invalid if it is not a string
        if check_all or 'description' in parameters:
            assert isinstance(self.description, str), "Description must be a string."

        # self.appendix is invalid if it is not a bytearray
        if check_all or 'appendix' in parameters:
            assert isinstance(self.appendix, bytearray), "Appendix must be a bytearray."

        # self.tags is invalid if it is not a list
        if check_all or 'tags' in parameters:
            assert isinstance(self.tags, list), "Tags must be a list."
            assert len(self.tags) == 3, "There must be 3 tags."

        # self.visibility is invalid if it is not an integer within the unsigned 8 bit limits
        if check_all or 'visibility' in parameters:
            assert isinstance(self.visibility, int), "Visibility must be an integer."
            assert Limits.U8_MIN <= self.visibility <= Limits.U8_MAX, "Visibility must be between 0 and 255."

        # self.seat is invalid if it is not None and there is no seat with that name
        if (check_all or 'seat' in parameters) and self.seat is not None:

            driver_seat_found: bool = False

            for brick in self.bricks:
                if brick.name == self.seat and brick.get_type() in _VALID_DRIVER_SEATS:
                    driver_seat_found = True

            assert driver_seat_found, "Specified driver seat not found."

        # self.creation_time is invalid if it is not an integer within the unsigned 64 bit limits
        if check_all or 'creation_time' in parameters:

            assert isinstance(self.creation_time, int), "Creation time must be an integer."
            assert Limits.U64_MIN <= self.creation_time <= Limits.U64_MAX, "Creation time must within the 64 bit unsigned integer range."

        if check_all or 'update_time' in parameters:

            assert isinstance(self.update_time, int), "Update time must be an integer."
            assert Limits.U64_MIN <= self.update_time <= Limits.U64_MAX, "Update time must within the 64 bit unsigned integer range."

        return self


    def backup(self, dst: str = BACKUP_FOLDER, name: str | None = None) -> Self:

        """
        Backup Brick Rigs' vehicle folder.

        :param dst: Directory where the backup will be stored.
        :param name: Name of the folder in which all Brick Rigs file (Vehicle.brv etc.) will be stored.

        :return: self
        """

        # TODO: CHECK IF THIS IS VALID FOR POSIX SYSTEMS.

        folder_name = str(get_time_100ns()) if name is None else name

        # Assert everything is valid
        self.assert_valid_parameters('project_name', 'project_dir')
        assert os.path.exists(dst), "Backup folder not found."

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



class Creation14(_Creation):

    def __init__(self, project_name: str, project_dir: str,
                 name: str = '', description: str = '', appendix: bytearray = bytearray(), tags: list[str] | None = None,
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

        super().__init__(project_name, project_dir)

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
        self.appendix: bytearray = appendix

        # Other
        self.visibility: int = visibility

        self.bricks: list[Brick14] = []

        # Private
        self.__BRV_VERSION: Final[int] = 14
