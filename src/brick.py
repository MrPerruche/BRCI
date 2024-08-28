from typing import Self, Optional
# from collections.abc import MutableMapping, MutableSequence
from copy import deepcopy
from .bricks import *

# from typing import Any -> from .bricks.bricks_utils


def _has_valid_properties(default_settings: dict[str, Any], property_map: dict[str, str], properties: dict[str, Any]) -> bool:

    for property_, value in properties.items():

        if property_ not in property_map.keys():
            return False




class _Brick:

    def __init__(self,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        """
        Internal class, blank brick object. Will store all data for a single brick.

        :param brick_type: Type of the brick.
        :type brick_type: str
        :param name: Name or identifier of the brick.
        :type name: str or int
        :param position: (x, y, z) coordinates of the brick's position.
        :type position: Optional[list[float, float, float]]
        :param rotation: (pitch, yaw, roll) angles in degrees for the brick's rotation.
        :type rotation: Optional[list[float, float, float]]
        :param properties: Additional properties of the brick as key-value pairs.
        :type properties: Optional[dict[str, Any]]
        """

        # Set all variables
        self._brick_type = brick_type
        self.name: str | int = name
        self.position: list[float] = [0.0, 0.0, 0.0] if position is None else position
        self.rotation: list[float] = [0.0, 0.0, 0.0] if rotation is None else rotation
        self.properties: dict[str, Any] = {} if properties is None else properties

        # Set properties to something meaningful (will keep already set properties if they've valid!)
        self.set_type(brick_type)


    def get_type(self) -> str:

        """
        Returns the type of the brick.

        :return: Type of the brick.
        :rtype: str
        """

        return self._brick_type


    def is_valid_brick(self) -> bool:

        """
        Checks if it is valid

        :return: True if it is valid else False
        :rtype: bool
        """

        raise NotImplementedError("Blank class. This function depends on the Brick version.")


    def set_type(self, new_type: str) -> Self:

        """
        Change the brick to another type.

        :param new_type: Type of the brick.

        :return: self
        :rtype: Brick
        """

        raise NotImplementedError("Blank class. This function depends on the Brick version.")


class Brick14(_Brick):

    def __init__(self,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        """
        Brick class for version 14 (Brick Rigs 1.7.0+).

        :param brick_type: Type of the brick.
        :type brick_type: str
        :param name: Name or identifier of the brick.
        :type name: str or int
        :param position: (x, y, z) coordinates of the brick's position.
        :type position: Optional[list[float, float, float]]
        :param rotation: (pitch, yaw, roll) angles in degrees for the brick's rotation.
        :type rotation: Optional[list[float, float, float]]
        :param properties: Additional properties of the brick as key-value pairs.
        :type properties: Optional[dict[str, Any]]
        """

        super().__init__(brick_type, name, position, rotation, properties)


    def is_valid_brick(self) -> int:

        # Doc inherited from _Brick.is_valid_brick()

        assert isinstance(self.name, (str, int)), "Name must be a string or an integer"

        # Integers are tolerated for position and rotation
        assert (isinstance(self.position, list) and len(self.position) == 3 and
                all(isinstance(x, (float, int)) for x in self.position)), "Position must be a list of 3 floats"
        assert (isinstance(self.rotation, list) and len(self.rotation) == 3 and
                all(isinstance(x, (float, int)) for x in self.rotation)), "Rotation must be a list of 3 floats"

        # Check properties




        return 1


    def set_type(self, new_type: str) -> Self:

        # Doc inherited from _Brick.set_type()

        # Make sure this brick exists
        if new_type in bricks14.keys():

            # Get new set of properties
            new_properties: dict[str, Any] = deepcopy(bricks14[new_type])

            for property_ in self.properties.keys():
                if property_ in new_properties:
                    new_properties[property_] = self.properties[property_]

            # Edit self for the new brick type
            self.properties = new_properties
            self._brick_type = new_type

        else:
            raise ValueError(f"Brick type {new_type!r} does not exist")

        return Self