from abc import ABC

from .creation import *
from ..brick import *
from ..utils import BRICK_RIGS_FOLDER
from ..constants import Visibility


class ModernCreation(Creation, ABC):


    # Method positions:

    # 1. Dunder methods (__init__ then alphabetical order)
    # 2. Getters / Setters (alphabetical order)
    # 3. Other (alphabetical order)


    def __init__(self, file_version: int, project_name: str, project_dir: str,
                 name: str = '', description: str = '', appendix: bytes | bytearray = bytearray(),
                 tags: list[str] | None = None, visibility: Visibility = Visibility.PUBLIC,
                 seat: Optional[str | int] = None,
                 creation_time: Optional[int] = None, update_time: Optional[int] = None,
                 size: Optional[list[float]] = None, weight: float = 0.0, price: float = 0.0, author: int = 0) -> None:

        super().__init__(file_version, project_name, project_dir)

        self.name: str = name
        self.description: str = description

        self.tags: list[str] = ["None", "None", "None"] if tags is None else tags

        self.creation_time: Optional[int] = creation_time
        self.update_time: Optional[int] = update_time
        self.size: list[float] = [0.0, 0.0, 0.0] if size is None else size
        self.price: float = price
        self.weight: float = weight
        self.author: int = author

        # File
        self.seat: Optional[str | int] = seat
        self.appendix: bytes | bytearray = appendix

        # Other
        self.visibility: Visibility = visibility

        self.bricks: list[Brick] = []





    @classmethod
    def get_brick_rigs_vehicle_folder(cls, potential_folders: Optional[list[str]] = None) -> str:

        """
        Will return the path to the BrickRigs vehicle folder to be used as project_dir argument.

        Arguments:
            potential_folders (Optional[list[str]], optional): Override list of potential folders.

        Exceptions:
            FileNotFoundError: When BrickRigs folder is not found.

        Returns:
            str: Path
        """

        return super().get_brick_rigs_vehicle_folder(BRICK_RIGS_FOLDER if potential_folders is None else potential_folders)



    @abstractmethod
    def deserialize_metadata(self, file: bytearray, load_last_update: bool = False):

        """
        Will read as a metadata file the given bytearray.

        Arguments:
            file (bytearray): Name of the file to read.
            load_last_update (bool, optional): If True, it will also load the last update timestamp.

        Returns:
            Self

        Exceptions:
            OverflowError: One of the values are invalid causing an overflow error.
            UnicodeEncodeException: One of the values are invalid causing a decoding error.
        """
        pass



    def read_metadata(self, file_name: str = 'MetaData.brm', load_last_update: bool = False) -> Self:

        """
        Will read the metadata file.

        Arguments:
            file_name (str): Name of the file to read.
            load_last_update (bool): If True, it will also load the last update timestamp.

        Returns:
            Self

        Exceptions:
            OverflowError: One of the values are invalid causing an overflow error.
            UnicodeEncodeException: One of the values are invalid causing a decoding error.
        """

        read_path = os.path.join(self.get_full_path(), file_name)

        if not os.path.exists(read_path):
            raise FileNotFoundError(f"File {file_name} not found")

        with open(read_path, 'rb') as f:
            self.deserialize_metadata(bytearray(f.read()), load_last_update)

        return self


    def rename_bricks(self, func: Callable[[str | int], str | int]) -> Self:

        """
        Will rename bricks using given a function

        Arguments:
            func (Callable[[str | int], str | int]): function giving new names for bricks according to their current name

        Returns:
            Self
        """

        # Create a map of all bricks
        names: dict = {brick.name: func(brick.name) for brick in self.bricks}

        for brick in self.bricks:
            # Change brick name
            brick.name = names[brick.name]
            # Change properties
            for key, value in brick.properties.items():
                # Note: if it shouldn't do anything, switch_names return value argument by default.
                brick.properties[key] = self.get_property_types_dict()[key].switch_names(value, names)

        return self



    @abstractmethod
    def serialize_metadata(self) -> bytearray:

        """
        Will generate metadata and return it as a bytearray

        Returns:
            bytearray: Metadata file
        """

        pass



    def write_metadata(self, file_name: str = 'MetaData.brm', exist_ok: bool = True):

        """
        Will generate and write the metadata file

        Arguments:
            file_name (str, optional): Name of the file to write.
            exist_ok (bool, optional): If True, will overwrite the file if it already exists.

        Exceptions:
            * Exceptions from .serialize_metadata()
            FileExistsError: File already exists and exist_ok is set to False

        Returns:
            Self
        """

        write_path: str = os.path.join(self.get_full_path(), file_name)

        if not exist_ok and os.path.exists(write_path):
            raise FileExistsError(f"Following file already exists: {write_path}")

        if not os.path.exists(self.get_full_path()):
            os.makedirs(self.get_full_path(), exist_ok=exist_ok)

        with open(write_path, 'wb') as f:
            f.write(self.serialize_metadata())

        return self



    def write_preview(self, image_path: str, file_name: str = 'Preview.png', exist_ok: bool = True) -> Self:

        """
        Will write preview for a file. A few default previews are included in brci. See brci.BRCI_THUMBNAIL, ...

        Arguments:
            image_path (str): Path to the image.
            file_name (str): Name of the file to write.
            exist_ok (bool): If True, will overwrite the file if it already exists.

        Returns:
            Self

        Exceptions:
            OSError: Image not found
            OSError: Preview already exists
        """

        # ################### VERIFYING PATHS ####################

        if not os.path.exists(image_path):
            raise OSError(f"Image missing {image_path}.")

        # TODO CHECK FOR PATH & NAME VALIDITY

        write_path = os.path.join(self.get_full_path(), file_name)

        if not exist_ok and os.path.exists(write_path):
            raise OSError(f"Invalid path {write_path}")

        # ################### WRITING IMAGE ####################

        with open(image_path, 'rb') as f:
            image = f.read()

        with open(write_path, 'wb') as f:
            f.write(image)

        return self