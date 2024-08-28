# from collections.abc import MutableMapping, MutableSequence
from typing import Final
from datetime import datetime, timezone
import os.path
import re
import numpy as np

# -------------------- DATA --------------------

# Version
BRCI_VERSION: str = "D1"  # D(...) is basically 4.(...)
BRICK_RIGS_VERSION: str = "1.7.4"

# Paths
_CWD: str = os.path.dirname(os.path.realpath(__file__))
_LOCALAPPDATA: str = os.getenv("LOCALAPPDATA")

if os.name == 'nt':
    _USER: str = os.getenv('%USERNAME%')
    BRICK_RIGS_FOLDER: list[str] = [os.path.join(_LOCALAPPDATA, 'BrickRigs', 'SavedRemastered', 'Vehicles')]
else:
    _USER: str = os.getenv('$USER')
    BRICK_RIGS_FOLDER: list[str] = [
        os.path.expanduser(f"~/.steam/steamapps/compatdata/552100/pfx/drive_c/users/steamuser/AppData/Local/BrickRigs/SavedRemastered/Vehicles"),
        os.path.expanduser(f"~/.wine/drive_c/users/{_USER}/AppData/Local/BrickRigs/SavedRemastered/Vehicles"),
        os.path.expanduser(f"~/.local/share/Steam/steamapps/compatdata/552100/pfx/drive_c/users/steamuser/AppData/Local/BrickRigs/SavedRemastered/Vehicles")
    ]

PROJECT_FOLDER: str = os.path.join(_CWD, 'Projects')
BACKUP_FOLDER: str = os.path.join(_CWD, 'Backups')


class Limits:

    """
    Class for holding integer and floating-point limits.

    :var U8_MAX: Maximum unsigned 8-bit integer (255)
    :var U16_MAX: Maximum unsigned 16-bit integer (65535)
    :var U32_MAX: Maximum unsigned 32-bit integer (4294967295)
    :var U64_MAX: Maximum unsigned 64-bit integer (18446744073709551615)

    :var I8_MAX: Maximum signed 8-bit integer (127)
    :var I16_MAX: Maximum signed 16-bit integer (32767)
    :var I32_MAX: Maximum signed 32-bit integer (2147483647)
    :var I64_MAX: Maximum signed 64-bit integer (9223372036854775807)

    :var U8_MIN: Minimum unsigned 8-bit integer (0)
    :var U16_MIN: Minimum unsigned 16-bit integer (0)
    :var U32_MIN: Minimum unsigned 32-bit integer (0)
    :var U64_MIN: Minimum unsigned 64-bit integer (0)

    :var I8_MIN: Minimum signed 8-bit integer (-128)
    :var I16_MIN: Minimum signed 16-bit integer (-32768)
    :var I32_MIN: Minimum signed 32-bit integer (-2147483648)
    :var I64_MIN: Minimum signed 64-bit integer (-9223372036854775808)
    """

    # Integer limits
    U8_MAX: Final[int] = np.iinfo(np.uint8).max
    U16_MAX: Final[int] = np.iinfo(np.uint16).max
    U32_MAX: Final[int] = np.iinfo(np.uint32).max
    U64_MAX: Final[int] = np.iinfo(np.uint64).max

    I8_MAX: Final[int] = np.iinfo(np.int8).max
    I16_MAX: Final[int] = np.iinfo(np.int16).max
    I32_MAX: Final[int] = np.iinfo(np.int32).max
    I64_MAX: Final[int] = np.iinfo(np.int64).max

    U8_MIN: Final[int] = 0
    U16_MIN: Final[int] = 0
    U32_MIN: Final[int] = 0
    U64_MIN: Final[int] = 0

    I8_MIN = np.iinfo(np.int8).min
    I16_MIN = np.iinfo(np.int16).min
    I32_MIN = np.iinfo(np.int32).min
    I64_MIN = np.iinfo(np.int64).min

    # Floating-point limits
    F32_MAX = np.finfo(np.float32).max
    F64_MAX = np.finfo(np.float64).max

    F32_MIN = np.finfo(np.float32).min
    F64_MIN = np.finfo(np.float64).min


def get_time_100ns() -> int:

    """
    Get the current time in 100 nanoseconds. Notably used in metadata and for BRCI backups.

    :return: 100s of nanoseconds since 0001-01-01 00:00:00
    :rtype: int
    """

    # Get current UTC time
    now = datetime.now(timezone.utc)
    # Calculate the time since year 1
    time_delta = now - datetime(1, 1, 1, tzinfo=timezone.utc)
    # Convert to 100 nanoseconds
    return int(time_delta.total_seconds() * 10**7)


def is_valid_folder_name(name: str, is_nt: bool) -> bool:

    """
    Check if the folder name is valid.

    :param name: Potentially invalid name
    :param is_nt: True if we are working with NT, otherwise False (POSIX)

    :return: True if the name is valid, otherwise False
    :rtype: bool
    """

    if is_nt:
        # Check for NT system validity
        nt_match = r'[<>:"/\\|?*]'
        if re.search(nt_match, name) or len(name) == 0 or set(name) == set() or name[-1] in {'.', ' '} or name in (
                "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
                "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"):
            return False
    else:
        # Check for POSIX system validity
        posix_match = r'[<>:"/\\|?*\x00-\x1F]'
        if re.search(posix_match, name):
            return False

    # else: valid
    return True
