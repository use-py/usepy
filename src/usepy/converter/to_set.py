from typing import Any
from .to_list import to_list


def to_set(value: Any) -> set:
    """Convert a value to a set.

    Args:
        value (Any): The value to convert.

    Returns:
        set: The set value.
    """
    if isinstance(value, set):
        return value
    return set(to_list(value))
