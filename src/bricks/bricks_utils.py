from typing import Any


def _add_mk(var: dict, keys: tuple[str, ...], value: Any) -> None:

    """
    Internal function to add to a dictionary multiple keys set to a single value.

    :param var: Dictionary to add to.
    :param keys: Keys to add.
    :param value: Value to set all keys to.

    :return: Nothing
    :rtype: None
    """

    for key in keys:
        var.setdefault(key, value)