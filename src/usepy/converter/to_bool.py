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
        >>> to_bool(1)
        True
        >>> to_bool(0)
        False
        >>> to_bool("no")
        False
        >>> to_bool(None)
        False
    """
    if value is None:
        return False
    if isinstance(value, bool):
        return value
    if isinstance(value, (int, float)):
        return bool(value)
    if isinstance(value, str):
        value = value.lower().strip()
        return value in ("yes", "true", "t", "y", "1", "on", "enabled")
    return bool(value)
