from typing import Any


def to_bool(value: Any) -> bool:
    """Convert a value to a boolean.

    Args:
        value (Any): The value to convert.

    Returns:
        bool: The boolean value.

    Examples:
        >>> to_bool(True)
        True
        >>> to_bool("True")
        True
        >>> to_bool("true")
        True
        >>> to_bool("t")
        True
    """
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        return value.lower() in ("yes", "true", "t", "y", "1")
    return bool(value)
