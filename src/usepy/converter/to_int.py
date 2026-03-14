from typing import Any, Optional


def to_int(value: Any, default: Optional[int] = None) -> Optional[int]:
    """
    Safely converts a value to an integer.

    Args:
        value (Any): The value to convert.
        default (Optional[int]): The default value to return if conversion fails. Defaults to None.

    Returns:
        Optional[int]: The integer value, or default if conversion fails.

    Examples:
        >>> to_int('123')
        123
        >>> to_int('abc', default=0)
        0
        >>> to_int(45.67)
        45
        >>> to_int(None)
        None
    """
    if value is None:
        return default
    try:
        return int(value)
    except (ValueError, TypeError):
        return default


def to_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    """
    Safely converts a value to a float.

    Args:
        value (Any): The value to convert.
        default (Optional[float]): The default value to return if conversion fails. Defaults to None.

    Returns:
        Optional[float]: The float value, or default if conversion fails.

    Examples:
        >>> to_float('123.45')
        123.45
        >>> to_float('abc', default=0.0)
        0.0
        >>> to_float(123)
        123.0
        >>> to_float(None)
        None
    """
    if value is None:
        return default
    try:
        return float(value)
    except (ValueError, TypeError):
        return default