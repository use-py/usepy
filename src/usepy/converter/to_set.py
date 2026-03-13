from typing import Any
from .to_list import to_list


def to_set(value: Any) -> set:
    """Convert a value to a set.

    Args:
        value (Any): The value to convert.

    Returns:
        set: The set value.

    Examples:
        >>> to_set(None)
        set()
        >>> to_set([1, 2, 2, 3])
        {1, 2, 3}
        >>> to_set((1, 2, 2, 3))
        {1, 2, 3}
    """
    if value is None:
        return set()
    if isinstance(value, set):
        return value
    return set(to_list(value))
