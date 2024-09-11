from typing import Final, Optional, Any
from datetime import datetime, timezone
import os.path
import re
import numpy as np
from builtins import print as printb

BRCI_VERSION: str = "D6"  # D(...) is basically 4.(...)
FM_ALIASES = True         # FM attributes in lowercase

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

NO_THUMBNAIL: str = os.path.join(_CWD, 'resources', 'no_thumbnail.png')
BRCI_THUMBNAIL: str = os.path.join(_CWD, 'resources', 'brci.png')

# Settings
settings: dict[str, Any] = {
    'show_logs': True,
    'attempt_error_mitigation': True
}

class FM:

    """
    Class containing various formatting features.
    """

    BLACK: Final[str] = '\033[30m'
    RED: Final[str] = '\033[91m'
    GREEN: Final[str] = '\033[92m'
    YELLOW: Final[str] = '\033[93m'
    BLUE: Final[str] = '\033[94m'
    MAGENTA: Final[str] = '\033[95m'
    CYAN: Final[str] = '\033[96m'
    WHITE: Final[str] = '\033[97m'
    LIGHT_BLACK: Final[str] = '\033[90m'
    LIGHT_RED: Final[str] = '\033[91m'
    LIGHT_GREEN: Final[str] = '\033[92m'
    LIGHT_YELLOW: Final[str] = '\033[93m'
    LIGHT_BLUE: Final[str] = '\033[94m'
    LIGHT_MAGENTA: Final[str] = '\033[95m'
    LIGHT_CYAN: Final[str] = '\033[96m'
    LIGHT_WHITE: Final[str] = '\033[97m'

    BOLD: Final[str] = '\033[1m'
    UNDERLINE: Final[str] = '\033[4m'
    ITALIC: Final[str] = '\033[3m'
    REVERSE: Final[str] = '\033[7m'
    STRIKETHROUGH: Final[str] = '\033[9m'

    CLEAR_ALL: Final[str] = '\033[0m'
    CLEAR_BOLD: Final[str] = '\033[22m'
    CLEAR_UNDERLINE: Final[str] = '\033[24m'
    CLEAR_ITALIC: Final[str] = '\033[23m'
    CLEAR_REVERSE: Final[str] = '\033[27m'
    CLEAR_STRIKETHROUGH: Final[str] = '\033[29m'

    # Function that outputs an error message
    @staticmethod
    def error(message: str, details: Optional[str] = None, force_print: bool = False) -> bool:

        """
        Will print an error message if show_logs is set to True.

        :param message: Header of the error, reversed.
        :param details: Details of the error, not reversed. If omitted (set to None), details will be omitted and the message will not be reversed.
        :param force_print: Will print regardless of what show_logs is set to.

        :return: True if the message was printed, else False.
        :rtype: bool
        """

        # Printing
        if force_print or settings['show_logs']:

            # If we specified details
            if details is not None:
                print(f'{FM.RED}{FM.REVERSE}[ERROR] {message}{FM.CLEAR_REVERSE} \n{details}')
            # If we did not specify details
            else:
                print(f'{FM.RED}{FM.REVERSE}[ERROR]{FM.CLEAR_REVERSE} {message}')

            # Either way, the message was printed
            return True

        # else:
        return False

    @staticmethod
    def success(message: str, details: Optional[str] = None, force_print: bool = False) -> bool:

        """
        Will print a success message if show_logs is set to True.

        :param message: Header of the success, reversed.
        :param details: Details of the success, not reversed. If omitted (set to None), details will be omitted and the message will not be reversed.
        :param force_print: Will print regardless of what show_logs is set to.

        :return: True if the message was printed, else False.
        :rtype: bool
        """

        if force_print or settings['show_logs']:

            # If we specified details
            if details is not None:
                print(f'{FM.LIGHT_GREEN}{FM.REVERSE}[SUCCESS] {message}{FM.CLEAR_REVERSE} \n{details}{FM.CLEAR_ALL} ')
            # If we did not specify details
            else:
                print(f'{FM.LIGHT_GREEN}{FM.REVERSE}[SUCCESS]{FM.CLEAR_REVERSE} {message}{FM.CLEAR_ALL} ')

            # Either way, the message was printed
            return True

        # else:
        return False

if FM_ALIASES:
    for attribute_name in dir(FM):
        if not attribute_name.startswith('_'):
            setattr(FM, attribute_name.lower(), getattr(FM, attribute_name))

print(f"{FM.LIGHT_GREEN}green text, constant naming{FM.CLEAR_ALL}")
print(f"{FM.light_green}green text, non-constant naming{FM.clear_all}")

def printr(*args, end="\n", **kwargs):
    """Print-Reset-Return. Resets color. Also, will return the text passed to it."""
    printb(*args, end=f"{end}{FM.CLEAR_ALL}", **kwargs)
    # return the exact text passed to print
    return_str = ""
    for arg in args:
        return_str += str(arg) + " "
    return repr(return_str.strip()) # sanitization: do not keep color codes in the return string

variable = printr(f"{FM.light_blue}some colored text right here")
print(f"non colored text, printr returned var: {variable}")