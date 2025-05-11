from datetime import datetime, timezone
from typing import Final, Optional
from builtins import print as _printb, input as _inputb
import re

from .data import settings


def clamp(min_val: float, x: float, max_val: float) -> float:
    return max(min_val, min(x, max_val))


class FM:

    """
    Class containing various formatting features.

    Variables:
        BLACK (Final[str]): ANSI escape code for black text
        RED (Final[str]): ANSI escape code for red text
        GREEN (Final[str]): ANSI escape code for green text
        YELLOW (Final[str]): ANSI escape code for yellow text
        BLUE (Final[str]): ANSI escape code for blue text
        MAGENTA (Final[str]): ANSI escape code for magenta text
        CYAN (Final[str]): ANSI escape code for cyan text
        WHITE (Final[str]): ANSI escape code for white text
        LIGHT_BLACK (Final[str]): ANSI escape code for light black (gray) text
        LIGHT_RED (Final[str]): ANSI escape code for light red text
        LIGHT_GREEN (Final[str]): ANSI escape code for light green text
        LIGHT_YELLOW (Final[str]): ANSI escape code for light yellow text
        LIGHT_BLUE (Final[str]): ANSI escape code for light blue text
        LIGHT_MAGENTA (Final[str]): ANSI escape code for light magenta text
        LIGHT_CYAN (Final[str]): ANSI escape code for light cyan text
        LIGHT_WHITE (Final[str]): ANSI escape code for light white (bright white) text
        BOLD (Final[str]): ANSI escape code for bold text
        UNDERLINE (Final[str]): ANSI escape code for underlined text
        ITALIC (Final[str]): ANSI escape code for italic text
        REVERSE (Final[str]): ANSI escape code for reversed text
        STRIKETHROUGH (Final[str]): ANSI escape code for strikethrough text
        CLEAR_ALL (Final[str]): ANSI escape code for clearing all formatting
        CLEAR_COLOR (Final[str]): ANSI escape code for clearing color formatting
        CLEAR_BOLD (Final[str]): ANSI escape code for clearing bold formatting
        CLEAR_UNDERLINE (Final[str]): ANSI escape code for clearing underlined formatting
        CLEAR_ITALIC (Final[str]): ANSI escape code for clearing italic formatting
        CLEAR_REVERSE (Final[str]): ANSI escape code for clearing reversed formatting
        CLEAR_STRIKETHROUGH (Final[str]): ANSI escape code for clearing strikethrough formatting
    """

    BLACK: Final[str] = '\033[30m'
    RED: Final[str] = '\033[31m'
    GREEN: Final[str] = '\033[32m'
    YELLOW: Final[str] = '\033[33m'
    BLUE: Final[str] = '\033[34m'
    MAGENTA: Final[str] = '\033[35m'
    CYAN: Final[str] = '\033[36m'
    WHITE: Final[str] = '\033[37m'
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
    CLEAR_COLOR: Final[str] = '\033[39m'
    CLEAR_BOLD: Final[str] = '\033[22m'
    CLEAR_UNDERLINE: Final[str] = '\033[24m'
    CLEAR_ITALIC: Final[str] = '\033[23m'
    CLEAR_REVERSE: Final[str] = '\033[27m'
    CLEAR_STRIKETHROUGH: Final[str] = '\033[29m'


    @staticmethod
    def rgb(r: int, g: int, b: int) -> str:

        """
        Will output the ansi escape code for RGB text.

        Arguments:
            r (int): red (0-255)
            g (int): green (0-255)
            b (int): blue (0-255)

        Returns:
            str: ANSI escape code
        """

        # "this is an insult to human intelligence" - Kira

        return f'\033[38;2;{r};{g};{b}m'

    # Function that outputs an error message
    @staticmethod
    def error(message: str, details: Optional[str] = None, force_print: bool = False) -> bool:

        """
        Will print an error message if show_logs is set to True.

        Arguments:
            message (str): Header of the error.
            details (Optional[str], optional): Details of the error, not reversed. If omitted (set to None), details will be omitted and the message will not be reversed.
            force_print (bool, optional): Will print regardless of what show_logs is set to. Defaults to False.

        Returns:
            bool: True if the message was printed, else False.
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

        Arguments:
            message (str): Header of the success.
            details (Optional[str], optional): Details of the success, not reversed. If omitted (set to None), details will be omitted and the message will not be reversed.
            force_print (bool, optional): Will print regardless of what show_logs is set to. Defaults to False.

        Returns:
            bool: True if the message was printed, else False.
        """

        if force_print or settings['show_logs']:

            # If we specified details
            if details is not None:
                print(f'{FM.YELLOW}{FM.REVERSE}[WARN] {message}{FM.CLEAR_REVERSE} \n{details}{FM.CLEAR_ALL} ')
            # If we did not specify details
            else:
                print(f'{FM.YELLOW}{FM.REVERSE}[WARN]{FM.CLEAR_REVERSE} {message}{FM.CLEAR_ALL} ')

            # Either way, the message was printed
            return True

        # else:
        return False

    @staticmethod
    def warning(message: str, details: Optional[str] = None, force_print: bool = False) -> bool:

        """
        Will print a warning message if show_logs is set to True.

        Arguments:
            message (str): Header of the warning.
            details (Optional[str], optional): Details of the warning, not reversed. If omitted (set to None), details will be omitted and the message will not be reversed.
            force_print (bool, optional): Will print regardless of what show_logs is set to. Defaults to False.

        Returns:
            bool: True if the message was printed, else False.
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


def get_time_100ns() -> int:
    """
    Get the current time in hundreds of nanoseconds. Notably used in metadata and for BRCI backups.

    Returns:
        int: 100s of nanoseconds since 0001-01-01 00:00:00

    Exceptions:
        OSError: Failed to retrieve time
        OverflowError: Time is set past 8639-12-17 23:59:59. In this case BRCI is not your least concern.
    """

    # Get current UTC time
    now = datetime.now(timezone.utc)
    # Calculate the time since year 1
    time_delta = now - datetime(1, 1, 1, tzinfo=timezone.utc)
    # Convert to 100 nanoseconds
    return int(time_delta.total_seconds() * 10 ** 7)



def is_valid_folder_name(name: str, is_nt: bool) -> bool:
    """
    Check if the folder name is valid.

    Arguments:
        name (str): Name of the folder.
        is_nt (bool): True if we are working with NT, otherwise False (POSIX). Can be checked using `os.name == 'nt'`

    Returns:
        bool: True if the folder name is valid, otherwise False

    Exceptions:
        TypeError: name is not a string or is_nt is not a boolean
    """

    if not type(name) == str:
        raise TypeError("Folder name must be a string")

    if not type(is_nt) == bool:
        raise TypeError("is_nt must be a boolean")

    if is_nt:
        # Check for NT system validity
        # nt_match = r'[<>:"/\\|?*]'  # TODO figure out a better solution for path issues

        nt_match = r'[<>:"/|?*]'

        #
        # if re.search(nt_match, name): print("fuck you regex")
        # if len(name) == 0: print("fuck you len")
        # if set(name) == set(): print("fuck you sets")
        # if name[-1] in {'.', ' '}: print("fuck you last character")
        # if name in (
        #        "CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9",
        #        "LPT1", "LPT2", "LPT3", "LPT4", "LPT5", "LPT6", "LPT7", "LPT8", "LPT9"): print("fuck you banned strs")
        # Making these lines comments because I felt like it, and because it was a massive block of neon green string text for me :bob_troll:

        bad_folder_names = ("CON", "PRN", "AUX", "NUL", "COM1", "COM2", "COM3",
                            "COM4", "COM5", "COM6", "COM7", "COM8", "COM9", "LPT1", "LPT2", "LPT3", "LPT4", "LPT5",
                            "LPT6", "LPT7",
                            "LPT8",
                            "LPT9")  # Technically EVER SO SLIGHTLY less efficient to make this a full variable, but screw you, fight with me over it. More readable.

        if (re.search(nt_match, name[2:] if len(name) > 1 and name[1] == ':' else name) or
                len(name) == 0 or
                set(name) == set() or
                name[-1] in {'.', ' '} or
                name in bad_folder_names):
            # This name is invalid. Return False.
            # logwrap("warning", f"NT directory name check *failed*. Dirname: {name}")
            # If you have an issue with logs being here, let me know. These will help with debugging.
            # If you want to disable logs in random areas like these, they're usually set to debug, just set the logger to a higher level to filter them out.
            return False
        else:
            pass
            # Once again, let me know.
            # logwrap("info", f"NT directory name check *passed*. Dirname: {name}")

    else:
        # Check for POSIX system validity
        posix_match = r'[<>:"/\\|?*\x00-\x1F]'
        if re.search(posix_match, name) or len(name) == 0 or set(name) == set():
            # logwrap("warning", f"POSIX directory name check *failed*. Dirname: {name}")
            return False
        else:
            pass
            # logwrap("info", f"POSIX directory name check *passed*. Dirname: {name}")

    # else: valid
    return True


def printr(*args: object, end: str = '\n', sep: str = ' ', col: str = '', clear: str = FM.CLEAR_ALL, **kwargs):

    """
    Print-Reset-Return. Resets color after printing message.

    Arguments:
        *args (tuple): Arguments to print.
        end (str, optional): End of the print. Defaults to "\n".
        sep (str, optional): Separator between arguments. Defaults to " ".
        col (str, optional): Color to apply before print. Defaults to None.
        clear (str, optional): Color to clear after print. Defaults to FM.CLEAR_ALL.
    """

    _printb(f"{col}{sep.join([str(arg) for arg in args])}", end=f"{end}{clear}", **kwargs)

    # Not sure why this ever was a thing. Uncomment it if needed.
    # return_str = sep.join([str(arg) for arg in args])
    # return repr(return_str.strip())[len(col):-len(clear)] # sanitization: do not keep color codes in the return string


# Unused, for the sake of completeness
def inputr(prompt: str, col: str = '', input_format: str = FM.CLEAR_ALL, clear: Optional[str] = FM.CLEAR_ALL) -> str:

    """
    Input-Reset-Return. Resets color after printing message.

    Arguments:
        prompt (str): Prompt to print.
        col (str, optional): Color to apply before print. Defaults to None.
        input_format (str, optional): Color to apply after print for user input format. Defaults to FM.CLEAR_ALL.
        clear (Optional[str], optional): Color to clear after user input. Not printed if set to None. Defaults to FM.CLEAR_ALL.

    Returns:
        str: User input string.
    """

    result: str = _inputb(f'{col}{prompt}{input_format}')
    if clear is not None:
        _printb(clear, end='')
    return result
