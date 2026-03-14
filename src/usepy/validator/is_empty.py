from typing import Any


def is_empty(value: Any) -> bool:
    """
    Checks if a value is empty.

    Empty values include: None, empty string, empty list, empty dict, empty set, 0, False.

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if the value is considered empty, False otherwise.

    Examples:
        >>> is_empty(None)
        True
        >>> is_empty('')
        True
        >>> is_empty([])
        True
        >>> is_empty({})
        True
        >>> is_empty('hello')
        False
        >>> is_empty([1])
        False
    """
    if value is None:
        return True
    if isinstance(value, (str, bytes, bytearray)):
        # Strip whitespace before checking length
        if isinstance(value, str):
            value = value.strip()
        return len(value) == 0
    if isinstance(value, (list, tuple, set, dict)):
        return len(value) == 0
    # Check for numeric 0 and False
    if value == 0 or value is False:
        return True
    return False