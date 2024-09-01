from typing import Self, Optional
# from collections.abc import MutableMapping, MutableSequence
# from copy import deepcopy
from .bricks import *
from .utils import settings, FM, Limits, is_utf_encodable

# from typing import Any -> from .bricks.bricks_utils


def _has_valid_properties(default_settings: dict[str, Any], property_map: dict[str, str], properties: dict[str, Any], call_callables: bool = False) -> tuple[bool, str]:

    if properties.keys() != default_settings.keys():

        for key in properties.keys():
            if key not in default_settings:

                # Key shouldn't be there. Is it not supposed to be here or not supposed to be a thing?
                if key in property_map.keys():
                    return False, f'Property {key} is not a property of this brick.'
                else:
                    return False, f'Unknown property: {key}.'

        for key in default_settings.keys():
            if key not in properties:
                return False, f'Missing property: {key}.'

    for property_, value in properties.items():

        # Set value to analyzed value (to make sure no editions happens)
        analyzed_value = value

        # If it's a callable -> e.g. lambda functions
        if callable(value):

            # If we want to call it, call it
            if call_callables:
                analyzed_value = value()
            # Else don't (maybe because previous executions affect later executions?)
            else:
                continue

        # Get what type the property is (we already checked if it was of a valid type)
        prop_type = property_map[property_]

        # Binary: must be bytes or bytearray
        if prop_type == 'bin':
            if not isinstance(analyzed_value, (bytes, bytearray)):
                return False, f'Property {property_} must be bytes or bytearray.'

        # Boolean: must be a boolean
        elif prop_type == 'bool':
            if not isinstance(analyzed_value, bool):
                return False, f'Property {property_} must be a boolean.'

        # Brick id: must be a string or integers (bricks are represented with strings and integers)
        elif prop_type == 'brick_id':
            if not isinstance(analyzed_value, (str, int)):
                return False, f'Property {property_} must be a string or an integer.'

        # Float: must be a float
        elif prop_type == 'float':
            if not isinstance(analyzed_value, float):
                return False, f'Property {property_} must be a float.'

        # List[3*float]: must be a list of 3 floats
        elif prop_type == 'list[3*float]':
            if not isinstance(analyzed_value, list):
                return False, f'Property {property_} must be a list of 3 floats.'
            if len(analyzed_value) != 3:
                return False, f'Property {property_} must be a list of 3 floats.'
            if not all(isinstance(item, float) for item in analyzed_value):
                return False, f'Property {property_} must be a list of 3 floats.'

        # List[3*uint8]: must be a list of 3 integers between 0 and 255
        elif prop_type == 'list[3*uint8]':
            if not isinstance(analyzed_value, list):
                return False, f'Property {property_} must be a list of 3 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if len(analyzed_value) != 3:
                return False, f'Property {property_} must be a list of 3 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if not all(isinstance(item, int) for item in analyzed_value):
                return False, f'Property {property_} must be a list of 3 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if not all(Limits.U8_MIN <= item <= Limits.U8_MAX for item in analyzed_value):
                return False, f'Property {property_} must be a list of 3 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'

        # List[4*uint8]: must be a list of 4 integers between 0 and 255
        elif prop_type == 'list[4*uint8]':
            if not isinstance(analyzed_value, list):
                return False, f'Property {property_} must be a list of 4 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if len(analyzed_value) != 4:
                return False, f'Property {property_} must be a list of 4 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if not all(isinstance(item, int) for item in analyzed_value):
                return False, f'Property {property_} must be a list of 4 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if not all(Limits.U8_MIN <= item <= Limits.U8_MAX for item in analyzed_value):
                return False, f'Property {property_} must be a list of 4 integers between {Limits.U8_MIN} and {Limits.U8_MAX}.'

        # List[6*uint2]: must be a list of 6 integers between 0 and 3
        elif prop_type == 'list[6*uint2]':
            if not isinstance(analyzed_value, list):
                return False, f'Property {property_} must be a list of 6 integers between {Limits.U2_MIN} and {Limits.U2_MAX}.'
            if len(analyzed_value) != 6:
                return False, f'Property {property_} must be a list of 6 integers between {Limits.U2_MIN} and {Limits.U2_MAX}.'
            if not all(isinstance(item, int) for item in analyzed_value):
                return False, f'Property {property_} must be a list of 6 integers between {Limits.U2_MIN} and {Limits.U2_MAX}.'
            if not all(Limits.U2_MIN <= item <= Limits.U2_MAX for item in analyzed_value):
                return False, f'Property {property_} must be a list of 6 integers between {Limits.U2_MIN} and {Limits.U2_MAX}.'

        # List[brick_id]: must be a list of brick ids (either strings or integers)
        elif prop_type == 'list[brick_id]':
            if not isinstance(analyzed_value, list):
                return False, f'Property {property_} must be a list of brick ids (either strings or integers).'
            if not isinstance(analyzed_value, (str, int)):
                return False, f'Property {property_} must be a list of brick ids (either strings or integers).'

        # String (utf-8): must be a string encodable in utf-8
        elif prop_type == 'str8':
            if not isinstance(analyzed_value, str):
                return False, f'Property {property_} must be a string encodable in utf-8.'
            # Check if it is encodable in utf-8
            if not is_utf_encodable(analyzed_value):
                return False, f'Property {property_} must be a string encodable in utf-8.'

        # String (utf-16): must be a string encodable in utf-16.
        elif prop_type == 'strany':
            if not isinstance(analyzed_value, str):
                return False, f'Property {property_} must be a string encodable in utf-8 or utf-16.'
            # Check if it is encodable in utf-8 and utf-16
            if not is_utf_encodable(analyzed_value):
                return False, f'Property {property_} must be a string encodable in utf-8 or utf-16.'

        # Integer: must be an integer between 0 and 255
        elif prop_type == 'uint8':
            if not isinstance(analyzed_value, int):
                return False, f'Property {property_} must be an integer between {Limits.U8_MIN} and {Limits.U8_MAX}.'
            if not (Limits.U8_MIN <= analyzed_value <= Limits.U8_MAX):
                return False, f'Property {property_} must be an integer between {Limits.U8_MIN} and {Limits.U8_MAX}.'



class Brick14:

    def __init__(self,
                 brick_type: str,
                 name: str | int,
                 position: Optional[list[float]] = None,
                 rotation: Optional[list[float]] = None,
                 properties: Optional[dict[str, Any]] = None) -> None:

        """
        Will store all data for a single brick.

        :param brick_type: Type of the brick.
        :param name: Name or identifier of the brick.
        :param position: (x, y, z) coordinates of the brick's position.
        :param rotation: (pitch, yaw, roll) angles in degrees for the brick's rotation.
        :param properties: Additional properties of the brick as key-value pairs.
        """

        # Set all variables
        self._brick_type = brick_type
        self.name: str | int = name
        self.position: list[float] = [0.0, 0.0, 0.0] if position is None else position
        self.rotation: list[float] = [0.0, 0.0, 0.0] if rotation is None else rotation
        self.properties: dict[str, Any] = {} if properties is None else properties

        # Set properties to something meaningful (will keep already set properties if they've valid!)
        self.set_type(brick_type)


    def get_type(self):
        return self._brick_type


    def is_invalid_brick(self, call_callables: bool = False) -> list[str]:

        """
        Will return all invalid values for this brick.

        :param call_callables: If True, will call all callables in properties.
        :return: list of invalid values
        """

        # Doc inherited from _Brick.is_valid_brick()
        invalid_values: list[str] = []

        # Check for name: is a string or integer
        if not isinstance(self.name, (str, int)):
            invalid_values.append('name')

        # Check for position: is a list of 3 floats or integers
        if not (isinstance(self.position, list) or len(self.position) == 3 or
                all(isinstance(x, (float, int)) for x in self.position)):

            invalid_values.append('position')

        # Check for rotation: is a list of 3 floats or integers
        if not (isinstance(self.rotation, list) or len(self.rotation) == 3 or
                all(isinstance(x, (float, int)) for x in self.rotation)):

            invalid_values.append('rotation')

        # Check properties
        valid_properties, _ = _has_valid_properties(bricks14[self._brick_type], property_types14, self.properties, call_callables)
        if not valid_properties:

            invalid_values.append('properties')

        return invalid_values


    def set_type(self, new_type: str) -> Self:

        """
        Sets the brick to a new type. Attempts to preserve any property in common with the new brick.

        :param new_type: New type of the brick.
        :return: self
        """

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