from abc import ABC, abstractmethod
from typing import Self, Optional, TypeVar, Final, Iterable, Literal
# from collections.abc import MutableMapping, MutableSequence
# from copy import deepcopy
from .bricks import *
from .constants import Limits
from .write_utils import can_be_encoded_in_utf

# from typing import Any -> from .bricks.bricks_utils


class Brick(ABC):

    def __init__(self, version: int,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        """
        Will store all data for a single brick.

        Arguments:
            brick_type (str): Type of the brick.
            name (str | int): Name or identifier of the brick.
            position (Optional[list[float]], optional): (x, y, z) coordinates of the brick's position. Defaults to None.
            rotation (Optional[list[float]], optional): (pitch, yaw, roll) angles in degrees for the brick's rotation. Defaults to None.
            properties (Optional[dict[str, Any]], optional): Additional properties of the brick as key-value pairs. Defaults to None.

        Exceptions:
            ValueError: If the brick type does not exist
            TypeError: Name is of invalid type
        """

        if type(name) not in (str, int):
            raise TypeError(f"Name must be a string or integer, not {type(name).__name__}.")

        # Set all variables
        self._brick_type = brick_type
        self.name: str | int = name
        self.position: list[float] = [0.0, 0.0, 0.0] if position is None else position
        self.rotation: list[float] = [0.0, 0.0, 0.0] if rotation is None else rotation
        self.properties: dict[str, Any] = {} if properties is None else properties

        self.__FILE_VERSION: int = version

        # Set properties to something meaningful (will keep already set properties if they've valid!)
        self.set_type(brick_type)


    def __repr__(self):
        return f'Brick{self.__FILE_VERSION}({self._brick_type!r}, {self.name!r}, {self.position!r}, {self.rotation!r}, {self.properties!r})'


    @abstractmethod
    def get_brick_list(self) -> dict[str, Any]:
        """
        Will return a list of all bricks for this file version.
        """
        pass


    def get_file_version(self) -> int:

        """
        Will return the file version of the Brick object.

        Returns:
            int: File version number
        """

        return self.__FILE_VERSION


    def get_type(self) -> str:

        """
        Will return the brick type of the Brick object.

        Returns:
            str: Type of the Brick object
        """
        return self._brick_type


    def set_type(self, new_type: str) -> Self:

        """
        Sets the brick to a new type. Attempts to preserve any property in common with the new brick.

        Arguments:
            new_type (str): New type of the brick.

        Returns:
            Self

        Exceptions:
            NameError: if the new type does not exist
        """

        # Make sure this brick exists
        if new_type in self.get_brick_list().keys():

            # Get new set of properties
            new_prop: dict[str, Any] = deepcopy(self.get_brick_list()[new_type])

            for property_ in self.properties.keys():
                if property_ in new_prop:
                    new_prop[property_] = self.properties[property_]

            # Edit self for the new brick type
            self.properties = new_prop
            self._brick_type = new_type

        else:
            raise NameError(f"Brick type {new_type!r} does not exist")

        return self


    def copy(self):
        return deepcopy(self)


class Brick14(Brick):


    def __init__(self,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        super().__init__(14, brick_type, name, position, rotation, properties)


    def get_brick_list(self) -> dict[str, Any]:
        return bricks14


class Brick15(Brick):

    def __init__(self,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        super().__init__(15, brick_type, name, position, rotation, properties)


    def get_brick_list(self) -> dict[str, Any]:
        return bricks15




def help14(brick: str | Iterable[str] | None, is_rst: bool = False) -> None:

    if brick is None or brick == '*':
        for b in sorted(bricks14.keys()):
            help14(b, is_rst)
        return

    if type(brick) != str:
        # print(type(brick).__name__, brick)
        # Line below raises error for brick being None
        for b in brick:
            help14(b, is_rst)
        return

    if brick not in bricks14.keys():
        raise NameError(f"Unknown brick type {brick!r}")


    result: str = ''

    if is_rst:

        result += f'**{brick}**\n\n'

        # result += '.. code-block:: none\n\n'
        for prop, val in bricks14[brick].items():
            result += f'- {prop}: ``{val!r}``\n'

    else:

        result += f'Brick type: {brick}\n'
        result += f'Properties: {{\n{',\n'.join([f'    {prop!r}: {val!r}' for prop, val in bricks14[brick].items()])}\n}}'

    print(result)


def help15(brick: str | Iterable[str] | None, is_rst: bool = False) -> None:

    if brick is None or brick == '*':
        for b in sorted(bricks15.keys()):
            help15(b, is_rst)
        return

    if type(brick) != str:
        # print(type(brick).__name__, brick)
        # Line below raises error for brick being None
        for b in brick:
            help15(b, is_rst)
        return

    if brick not in bricks15.keys():
        raise NameError(f"Unknown brick type {brick!r}")


    result: str = ''

    if is_rst:

        result += f'**{brick}**\n\n'

        # result += '.. code-block:: none\n\n'
        for prop, val in bricks15[brick].items():
            result += f'- {prop}: ``{val!r}``\n'

    else:

        result += f'Brick type: {brick}\n'
        result += f'Properties: {{\n{',\n'.join([f'    {prop!r}: {val!r}' for prop, val in bricks15[brick].items()])}\n}}'

    print(result)