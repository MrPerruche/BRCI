from typing import SupportsBytes, Any
# from .brick import Brick


# ------------------- CREATION GENERATION ---------------------




def _convert_brick_types(brick_types: set[str]) -> bytearray:
    # Returns brick types to write
    buffer: bytearray = bytearray()
    for brick_type in brick_types:
        buffer.extend(unsigned_int(len(brick_type), 1))
        buffer.extend(utf8(brick_type))
    return buffer


# FIXME
def _get_property_data(bricks: list, default_properties: dict[str, Any]) -> (
        dict[int, str], dict[str, int], dict[int, dict[int, Any]], dict[int, dict[Any, int]]):

    """
    Internal function to transform property data into userful information for .brv file generation.

    :param bricks: List of bricks making the creation
    :param default_properties: Default properties of bricks. (e.g. expects bricks14 variable)
    :return:
        1. Conversion table: property id to type,
        2. Conversion table: type to property id,
        3. Conversion table: property id to (value id to value conversion table),
        4. Conversion table: property id to (value to value id conversion table)
    """

    # Init variables
    property_id_types: dict[int, str] = {}  # Property and their id
    property_types_id: dict[str, int] = {}  # Property id and their property
    property_id_values_id: dict[int, dict[int, Any]] = {}  # Property id and their values: id -> value
    property_id_values_value: dict[int, dict[Any, int]] = {}  # Property id and their values: value -> id

    for brick in bricks:

        # Cache brick type defaults
        brick_type_defaults: dict[str, Any] = default_properties[brick.get_type()]

        for property_, value in brick.properties.items():

            # Clarification:
            # - property_id_values_id[property_id] -> gets list of values dict[int, Any]
            # - default_properties[brick.get_type()][property_] -> default value for this brick and this property.

            # Skipping if set to default
            if brick_type_defaults[property_] == value: continue

            # Adding to list of known properties
            # is None if missing else id (int)
            property_id = property_types_id.get(property_)

            # If it is new
            if property_id is None:

                property_id = len(property_types_id)  # Give it an id

                property_id_types[property_id] = property_  # Initialize first property-to-id container
                property_types_id[property_] = property_id  # Initialize second id-to-property container
                # value_id[property_id] = 0

                property_id_values_id[property_id] = {}  # Initialize first id-to-value container
                property_id_values_value[property_id] = {}  # Initialize second value-to-id container

            # Storing values
            print(property_id_values_value)
            print(property_id_values_value[property_id])
            value_id: int | None = property_id_values_value[property_id].get(value)  # Error? Issue: value is mutable. FIXME

            if value_id is None:
                value_id = len(property_id_values_id[property_id])  # Give it an id
                property_id_values_id[property_id][value_id] = value  # Store id-to-value
                property_id_values_value[property_id][value] = value_id  # Store value-to-id

            # else: property is known so we can ignore it

    return property_id_types, property_types_id, property_id_values_id, property_id_values_value


# ------------------- GENERAL --------------------


def get_signed_int(bin_value: SupportsBytes) -> int:

    """
    Convert bytes to a signed integer.

    :param bin_value: Bytes
    :return: Signed integer
    """

    return int.from_bytes(bin_value, byteorder='little', signed=True)


def get_unsigned_int(bin_value: SupportsBytes) -> int:

    """
    Convert bytes to an unsigned integer.

    :param bin_value: Bytes
    :return: Unsigned integer
    """
    return int.from_bytes(bin_value, byteorder='little', signed=False)


def is_utf_encodable(string: str) -> bool:

    """
    Check if the string can be encoded in UTF-8 and UTF-16.

    :param string: String to be tested
    :return: True if the string can be encoded in UTF-8 and UTF-16, otherwise False
    """

    return all(ord(char) <= 0x10FFFF for char in string)


def signed_int(integer: int, byte_len: int) -> bytes:

    """
    Convert a signed integer to bytes.

    :param integer: Signed integer
    :param byte_len: Number of bytes in the integer
    :return: Bytes
    """

    if integer < 2**(byte_len*8-1):
        raise OverflowError(f'Input is less than {byte_len*8} bit limit of signed integer.')

    if integer >= 2**(byte_len*8-1):
        raise OverflowError(f'Input is greater than {byte_len*8} bit limit of signed integer.')

    return integer.to_bytes(byte_len, byteorder='little', signed=True)


def unsigned_int(integer: int, byte_len: int) -> bytes:

    """
    Convert an unsigned integer to bytes.

    :param integer: Unsigned integer
    :param byte_len: Number of bytes in the integer
    :return: Bytes
    """

    if integer >= 2**(byte_len*8):
        raise OverflowError(f'Input is greater than {byte_len*8} bit limit of unsigned integer.')

    if integer < 0:
        raise OverflowError(f'Negative input. {integer} is less than 0.')

    return (integer & ((1 << (8 * byte_len)) - 1)).to_bytes(byte_len, byteorder='little', signed=False)


def utf8(string: str) -> bytes:

    """
    Convert a string to UTF-8 bytes.

    :param string: String
    :return: Bytes
    """

    return string.encode('utf-8')


def utf16(string: str) -> bytes:

    """
    Convert a string to UTF-16 bytes.

    :param string: String
    :return: Bytes
    """

    return string.encode('utf-16')