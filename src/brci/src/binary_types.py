from abc import ABC, abstractmethod
from enum import Enum
from typing import Any, Literal, Optional
from collections.abc import Iterable
import numpy as np
from struct import unpack as _struct_unpack

from .constants import Connection
from .utils import ConnectorSpacing
def extract_bytes(ba: bytearray, n: int) -> bytearray:

    """
    Removes the first n bytes of the bytearray and returns them, or all if n is greater than the length of the bytearray.

    Arguments:
        ba (bytearray): Bytearray to extract from
        n (int): Number of bytes to extract

    Returns:
        bytearray: Extracted bytes
    """

    if n > len(ba): n = len(ba)

    result = ba[:n]
    del ba[:n]

    return result
def get_utf8(bin_value: bytes | bytearray) -> str:

    """
    Convert UTF-8 bytes to a string.

    Arguments:
        bin_value (bytes | bytearray): Bytes to convert (little-endian)

    Returns:
        str: String
    """
    return bin_value.decode('ascii')
def get_utf16(bin_value: bytes | bytearray) -> str:

    """
    Convert UTF-16 bytes to a string.

    Arguments:
        bin_value (bytes | bytearray): Bytes to convert (little-endian)

    Returns:
        str: String
    """

    return bin_value.decode('utf-16')



class BinaryType(ABC):

    @staticmethod
    @abstractmethod
    def serialize(value: Any, brick_id_table: dict[str | int, int]) -> bytearray:
        raise NotImplementedError("Subclasses must implement serialize() method.")

    @staticmethod
    @abstractmethod
    def deserialize(ba: bytearray, try_np: bool = False) -> Any:
        raise NotImplementedError("Subclasses must implement deserialize() method.")

    @staticmethod
    def switch_names(source: Any, name_table: dict[str | int, str | int]) -> Any:
        return source


class BinaryTypes:

    @staticmethod
    def serialize_safe_int(value: int, length: int, signed: bool, byteorder: Literal['big', 'little'] = 'little') -> bytearray:
        return bytearray(value.to_bytes(length, byteorder=byteorder, signed=signed))

    @staticmethod
    def serialize_int(value: int | np.integer, length: int, signed: bool, byteorder: Literal['big', 'little'] = 'little') -> bytearray:
        if isinstance(value, np.integer):
            value = value.item()
        # print(f'{value=}, {length=}, {signed=}, {byteorder=}, {(1<<(length*8))-1=}, {value & ((1<<(length*8))-1)=}')
        return bytearray(( value & ((1<<(length*8))-1) ).to_bytes(length, byteorder=byteorder, signed=signed))  # Little-endian

    @staticmethod
    def deserialize_safe_int(ba: bytearray, signed: bool, byteorder: Literal['big', 'little'] = 'little') -> int:
        return int.from_bytes(ba, byteorder=byteorder, signed=signed)

    @staticmethod
    def serialize_float32(value: float | np.floating) -> bytearray:
        if isinstance(value, (int, float)):
            value = np.float32(value)
        return bytearray(value.tobytes())

    @staticmethod
    def deserialize_float32(ba: bytearray) -> np.float32:
        return _struct_unpack('<f', ba[:4])[0]


    class BrickID(BinaryType):

        @staticmethod
        def serialize(value: Optional[int | str], brick_id_table: dict[str | int, int]) -> bytearray:
            if value is None:
                return bytearray(b'\x00\x00')
            # else:
            id_ = brick_id_table.get(value)
            if id_ is None:
                raise ValueError(f"Brick with ID {value} not found")
            return bytearray(b'\x00\x01') + BinaryTypes.serialize_safe_int(id_+1, 2, False)

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> int:
            value = BinaryTypes.deserialize_safe_int(ba[2:], False) - 1
            return None if value < 0 else value

        @staticmethod
        def switch_names(source: str | int, name_table: dict[str | int, str | int]):

            new_name = name_table.get(source)
            if new_name is None:
                raise ValueError(f"Brick with ID {source} not found in name table")
            return new_name

    # noinspection PyPep8Naming
    class List_BrickID(BinaryType):

        @staticmethod
        def serialize(value: list[int | str], brick_id_table: dict[str | int, int]) -> bytearray:
            result = BinaryTypes.serialize_int(len(value), 2, False)
            for val in value:
                id_ = brick_id_table.get(val)
                if id_ is None:
                    raise NameError(f"Brick with name {val} not found")
                result.extend(BinaryTypes.serialize_safe_int(id_+1, 2, False))
            return result

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = []
            for i in range(int.from_bytes(ba[0:2], byteorder='little')):
                value = BinaryTypes.deserialize_safe_int(ba[ 2+i*2 : 4+i*2 ], False) - 1
                result.append(None if value < 0 else value)
            return result

        @staticmethod
        def switch_names(source: str | int, name_table: dict[str | int, str | int]):
            result = []
            for val in source:
                if val is None: continue
                new_name = name_table.get(val)
                if new_name is None:
                    raise ValueError(f"Brick with ID {val} not found in name table")
                result.append(new_name)
            return result


    class Boolean(BinaryType):

        @staticmethod
        def serialize(value: bool, brick_id_table: dict[str | int, int]) -> bytearray:
            return bytearray(b'\x01') if value else bytearray(b'\x00')

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> bool:
            return bool(ba[0])


    class ConnectorSpacingLike(BinaryType):

        @staticmethod
        def serialize(value: int | np.integer | Iterable[int | np.integer] | ConnectorSpacing, brick_id_table: dict[str | int, int]) -> bytearray:

            result_int: int = 0

            if isinstance(value, ConnectorSpacing):
                for i, connection in enumerate(value):
                    result_int |= connection.value << (i * 2)
                return BinaryTypes.serialize_safe_int(result_int, 2, False)

            elif isinstance(value, (int, np.integer)):
                if not 0 <= value <= 0x00_FF_FF_FF:
                    raise ValueError(f"Invalid value")
                return BinaryTypes.serialize_int(value, 2, False)
            #else:

            i = 0
            for i, connection in enumerate(value):
                if not 0 <= connection <= 3:
                    raise ValueError(f"Invalid connection")
                result_int |= connection << (i * 2)
            if i != 5:  # Expecting 6 connections so i = 5 at the end if right
                raise ValueError(f"Expected 6 connections, not {i + 1}")
            return BinaryTypes.serialize_int(result_int, 2, False)

        @staticmethod
        def deserialize(ba: bytearray, context: Optional[dict[str, Any]] = None, try_np: bool = False) -> ConnectorSpacing:
            result_int: int = BinaryTypes.deserialize_safe_int(ba, False)
            # Split result into 6 2bit uints
            result_list = [Connection.from_int(result_int >> (i * 2) & 0b11) for i in range(6)]
            return ConnectorSpacing(result_list[1], result_list[3], result_list[5],
                                    result_list[0], result_list[2], result_list[4])


    class Float32(BinaryType):

        @staticmethod
        def serialize(value: float | np.floating, brick_id_table: dict[str | int, int]) -> bytearray:
            return BinaryTypes.serialize_float32(value)

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = BinaryTypes.deserialize_float32(ba)
            return result # if try_np else result.item()


    class List2_Float32(BinaryType):

        @staticmethod
        def serialize(value: list[float | np.floating], brick_id_table: dict[str | int, int]) -> bytearray:
            result = bytearray()
            if len(value) != 2:
                raise ValueError(f"Expected 2 floats, not {len(value)}")
            for val in value:
                result.extend(BinaryTypes.Float32.serialize(val, brick_id_table))
            return result

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = []
            for i in range(2):
                result.append(BinaryTypes.Float32.deserialize(ba[i*4:(i+1)*4], try_np))
            return result


    # noinspection PyPep8Naming
    class List3_Float32(BinaryType):

        @staticmethod
        def serialize(value: list[float | np.floating], brick_id_table: dict[str | int, int]) -> bytearray:
            result = bytearray()
            if len(value) != 3:
                raise ValueError(f"Expected 3 floats, not {len(value)}")
            for val in value:
                result.extend(BinaryTypes.Float32.serialize(val, brick_id_table))
            return result

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = []
            for i in range(3):
                result.append(BinaryTypes.Float32.deserialize(ba[i*4:(i+1)*4], try_np))
            return result


    class UInteger8(BinaryType):

        @staticmethod
        def serialize(value: int | np.integer, brick_id_table: dict[str | int, int]) -> bytearray:
            return BinaryTypes.serialize_int(value, 1, False)

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = BinaryTypes.deserialize_safe_int(ba, False)
            return result # if try_np else result.item()


    # noinspection PyPep8Naming
    class List3_UInteger8(BinaryType):

        @staticmethod
        def serialize(value: list[int | np.integer], brick_id_table: dict[str | int, int]) -> bytearray:
            result = bytearray()
            if len(value) != 3:
                raise ValueError(f"Expected 3 ints, not {len(value)}")
            for val in value:
                result.extend(BinaryTypes.UInteger8.serialize(val, brick_id_table))
            return result

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = []
            for i in range(3):
                result.append(BinaryTypes.UInteger8.deserialize(ba[i:i+1], try_np))
            return result


    # noinspection PyPep8Naming
    class List4_UInteger8(BinaryType):

        @staticmethod
        def serialize(value: list[int | np.integer], brick_id_table: dict[str | int, int]) -> bytearray:
            result = bytearray()
            if len(value) != 4:
                raise ValueError(f"Expected 4 ints, not {len(value)}")
            for val in value:
                result.extend(BinaryTypes.UInteger8.serialize(val, brick_id_table))
            return result

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = []
            for i in range(4):
                result.append(BinaryTypes.UInteger8.deserialize(ba[i:i+1], try_np))
            return result


    class UInteger16(BinaryType):

        @staticmethod
        def serialize(value: int | np.integer, brick_id_table: dict[str | int, int]) -> bytearray:
            return BinaryTypes.serialize_int(value, 2, False)

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = BinaryTypes.deserialize_safe_int(ba, False)
            return result # if try_np else result.item()


    class UInteger32(BinaryType):

        @staticmethod
        def serialize(value: int | np.integer, brick_id_table: dict[str | int, int]) -> bytearray:
            return BinaryTypes.serialize_int(value, 4, False)

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            result = BinaryTypes.deserialize_safe_int(ba, False)
            return result # if try_np else result.item()


    class StrictString(BinaryType):

        @staticmethod
        def serialize(value: str, brick_id_table: dict[str | int, int]) -> bytearray:

            try:
                if len(value) > 255:
                    raise ValueError("Provided string is too long.")
                converted = BinaryTypes.serialize_safe_int(len(value), 1, False)
                converted += value.encode('utf-8')
            except UnicodeEncodeError:
                raise ValueError("Provided string is not 8-bit ASCII.")
            return converted

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            return ba[1: ].decode('utf-8')


    class String(StrictString):

        @staticmethod
        def serialize(value: str | Enum, brick_id_table: dict[str | int, int]) -> bytearray:
            if isinstance(value, Enum):
                value = value.value
            return BinaryTypes.StrictString.serialize(value, brick_id_table)


    class Text(BinaryType):

        @staticmethod
        def serialize(value: str, brick_id_table: dict[str | int, int]) -> bytearray:
            try:
                if len(value) > 32767:
                    raise ValueError("Provided string is too long.")
                converted = BinaryTypes.serialize_safe_int(-len(value), 2, True)
                converted += value.encode('utf-16')[2: ]
            except UnicodeEncodeError:
                raise ValueError("Provided string is not UTF-16.")
            return converted

        @staticmethod
        def deserialize(ba: bytearray, try_np: bool = False) -> Any:
            str_len: int = BinaryTypes.deserialize_safe_int(extract_bytes(ba, 2), False)
            if str_len < 0:
                return get_utf16(extract_bytes(ba, -str_len))
            else:
                return get_utf8(extract_bytes(ba, str_len))




