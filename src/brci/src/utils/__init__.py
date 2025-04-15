# Not done yet # from .brick_types import *
from .data import *
from .enums import *
from .misc import *
from .property import *
from .write import *



# Temporarily removed content:

"""
try:
    import logging
    we_have_logging = True
except ImportError:
    print("`logging` module not found. Logging is a soft-dependency. Please install it, as it can greatly help the debugging process.")



if we_have_logging:
    # The import exists.
    logfile_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'brci.log')

    if os.path.exists(logfile_path):
        # Remove log file if it exists. By default, logging uses append.
        os.remove(logfile_path)

    logger = logging.getLogger("BRCI")
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler(logfile_path, mode="a", encoding="utf-8", errors="ignore") # For some godforsaken reason, if mode is not append, it doesn't log.
                                                                                                  # after this `if` statement. Period. No clue why.
                                                                                                  # DO NOT TOUCH. Black magic at work.
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    logger.info("Logging set up!")



def logwrap(level: Literal["info", "debug", "warning", "error", "critical"], msg: str) -> str:
    \"""
    A special function in place of the regular `logging` calls, as to not raise errors if `logging` is not found.

    Arguments:
        level (Literal["info", "debug", "warning", "error", "critical"]): The log level.
        msg (str): The message to log.

    Returns:
        str: The message logged. Good for using this function in print statements, function calls, variables, etc.
    \"""

    if we_have_logging:
        match level:
            case "info":
                logger.info(msg)
            case "debug":
                logger.debug(msg)
            case "warning":
                logger.warning(msg)
            case "error":
                logger.error(msg)
            case "critical":
                logger.critical(msg)
            case _:
                # Not a valid log level. Default to info with a warning message.
                logger.info(f"(Note: Invalid log level '{level}'!) || {msg}")
    else:
        print("Logwrap called, but logging disabled...")

    return msg
"""