from typing import Any


def to_list(value: Any) -> list:
    """Convert a value to a list.

    Args:
        value (Any): The value to convert.

    Returns:
        list: The list value.

    Examples:
        >>> to_list(None)
        []
        >>> to_list("abc")
        ['a', 'b', 'c']
        >>> to_list((1, 2))
        [1, 2]
        >>> to_list({1, 2})
        [1, 2]
        >>> to_list(1)
        [1]
    """
    if value is None:
        return []
    if isinstance(value, list):
        return value
    if isinstance(value, (str, bytes)):
        return list(value)
    try:
        return list(value)
    except TypeError:
        return [value]
