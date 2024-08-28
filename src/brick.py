from typing import Self, Optional
# from collections.abc import MutableMapping, MutableSequence
# from copy import deepcopy
from .bricks import *
from .utils import attempt_error_mitigation, FM, Limits

# from typing import Any -> from .bricks.bricks_utils


# TODO
def _has_valid_properties(default_settings: dict[str, Any], property_map: dict[str, str], properties: dict[str, Any]) -> (bool, str):

    if properties.keys() != default_settings.keys():

        for key in properties.keys():
            if key not in default_settings:
                if key in property_map.keys():
                    return False, f'Property {key} is not a property of this brick.'
                else:
                    return False, f'Unknown property: {key}.'

        for key in default_settings.keys():
            if key not in properties:
                return False, f'Missing property: {key}.'

    for property_, value in properties.items():

        match property_map[property_]:

            case 'brick_id':
                if not isinstance(value, (str, int)):
                    return False

            case 'list[4*uint8]':
                if not isinstance(value, list):
                    return False
                if len(value) != 4:
                    return False
                if not all(isinstance(item, int) for item in value):
                    return False
                if not all(Limits.U8_MIN <= item <= Limits.U8_MAX for item in value):
                    return False

            # TODO

# {'brick_id', 'list[4*uint8]', 'uint8', 'strany', 'list[brick_id]', 'str8', 'float', 'list[3*float]', 'list[6*uint2]', 'list[3*uint8]', 'bool'}


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


    def is_valid_brick(self, invalid_is_error: bool = False) -> bool:

        # Doc inherited from _Brick.is_valid_brick()

        if not isinstance(self.name, (str, int)):

            if not invalid_is_error:
                return False

            # else:
            # Signal there is something wrong
            FM.error("Brick name must be a string or an integer",
                     "Bricks must have as a name either a string or an integer.\n"
                     f"Brick name is: {self.name!r} (type: {type(self.name).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                try:
                    self.name = str(self.name)
                    FM.success(f"This brick is now named: {self.name!r} (type: {type(self.name).__name__}).")
                except ValueError:
                    raise ValueError(f"Brick name must be a string or an integer. Error mitigation failed.")

            else:
                raise ValueError("Brick name must be a string or an integer.")

        # Integers are tolerated for position and rotation
        # Position
        # If it is not a list
        if not isinstance(self.position, list):

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick position must be a list.",
                     "Bricks must have as a position a list.\n"
                     f"Brick position is: {self.position!r} (type: {type(self.position).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                try:
                    self.position = [float(x) for x in self.position]
                    FM.success(f"This brick's position is now set to: {self.position!r} (type: {type(self.position).__name__}).")
                except ValueError:
                    raise ValueError(f"Brick position must be a list. Error mitigation failed.")

            else:
                raise ValueError("Brick position must be a list.")

        # If it is not of the right length
        if not len(self.position) == 3:

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick position must be a list of 3 floats",
                     "Bricks must have as a position a list of 3 floats.\n"
                     f"Brick position is: {self.position!r} (type: {type(self.position).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                if len(self.position) > 3:
                    self.position = self.position[:3]
                else:  # len(self.position) < 3
                    self.position = self.position + [0.0] * (3 - len(self.position))

                FM.success(f"This brick's position is now set to: {self.position!r} (type: {type(self.position).__name__}).")

            else:
                raise ValueError("Brick position must be a list.")

        # If its elements are not of the right type
        if not all(isinstance(x, (float, int)) for x in self.position):

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick position must be a list of 3 floats",
                     "Bricks must have as a position a list of 3 floats.\n"
                     f"Brick position is: {self.position!r} (type: {type(self.position).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                try:
                    self.position = [float(x) for x in self.position]
                    FM.success(f"This brick's position is now set to: {self.position!r} (type: {type(self.position).__name__}).")
                except ValueError:
                    raise ValueError(f"Brick position must be a list of 3 floats. Error mitigation failed.")

            else:
                raise ValueError("Brick position must be a list of 3 floats.")

        # Rotation
        # If it is not a list
        if not isinstance(self.rotation, list):

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick rotation must be a list.",
                     "Bricks must have as a rotation a list.\n"
                     f"Brick rotation is: {self.rotation!r} (type: {type(self.rotation).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                try:
                    self.rotation = [float(x) for x in self.rotation]
                    FM.success(f"This brick's rotation is now set to: {self.rotation!r} (type: {type(self.rotation).__name__}).")
                except ValueError:
                    raise ValueError(f"Brick rotation must be a list. Error mitigation failed.")

            else:
                raise ValueError("Brick rotation must be a list.")

        # If it is not of the right length
        if not len(self.rotation) == 3:

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick rotation must be a list of 3 floats",
                     "Bricks must have as a rotation a list of 3 floats.\n"
                     f"Brick rotation is: {self.rotation!r} (type: {type(self.rotation).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                if len(self.rotation) > 3:
                    self.rotation = self.rotation[:3]
                else:  # len(self.rotation) < 3
                    self.rotation = self.rotation + [0.0] * (3 - len(self.rotation))

                FM.success(f"This brick's rotation is now set to: {self.rotation!r} (type: {type(self.rotation).__name__}).")

            else:
                raise ValueError("Brick rotation must be a list of 3 floats.")

        # If its elements are not of the right type
        if not all(isinstance(x, (float, int)) for x in self.rotation):

            if not invalid_is_error:
                return False

            #else:
            # Signal there is something wrong
            FM.error("Brick rotation must be a list of 3 floats",
                     "Bricks must have as a rotation a list of 3 floats.\n"
                     f"Brick rotation is: {self.rotation!r} (type: {type(self.rotation).__name__}).")

            # See if we can fix the issue (if the user wants to)
            if attempt_error_mitigation:
                try:
                    self.rotation = [float(x) for x in self.rotation]
                    FM.success(f"This brick's rotation is now set to: {self.rotation!r} (type: {type(self.rotation).__name__}).")
                except ValueError:
                    raise ValueError(f"Brick rotation must be a list of 3 floats. Error mitigation failed.")

            else:
                raise ValueError("Brick rotation must be a list of 3 floats.")

        # Check properties
        is_valid, reason = _has_valid_properties(bricks14[self._brick_type], property_types14, self.properties)
        # TODO

        return True


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