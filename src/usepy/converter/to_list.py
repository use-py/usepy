from typing import Any


def to_list(value: Any) -> list:
    """Convert a value to a list.

    Args:
        value (Any): The value to convert.

    Returns:
        list: The list value.
    """
    if isinstance(value, list):
        return value
    if isinstance(value, (str, bytes)):
        return list(value)
    try:
        return list(value)
    except TypeError:
        return [value]
