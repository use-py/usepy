from typing import Any


def to_string(value: Any) -> str:
    """Convert a value to a string.

    Args:
        value (Any): The value to convert.

    Returns:
        str: The string value.
    """
    if value is None:
        return ""
    if isinstance(value, (list, tuple, set)):
        return ", ".join(map(to_string, value))
    if isinstance(value, dict):
        return ", ".join(f"{k}: {to_string(v)}" for k, v in value.items())
    return str(value)
