import re
from typing import Any


def is_email(email: str) -> bool:
    """
    Checks if a string is a valid email address.

    Args:
        email (str): The email string to validate.

    Returns:
        bool: True if valid email format, False otherwise.

    Examples:
        >>> is_email('user@example.com')
        True
        >>> is_email('invalid.email')
        False
        >>> is_email('')
        False
    """
    if not email:
        return False
    # Simple email regex for basic validation
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))


def is_json(json_string: str) -> bool:
    """
    Checks if a string is valid JSON.

    Args:
        json_string (str): The JSON string to validate.

    Returns:
        bool: True if valid JSON format, False otherwise.

    Examples:
        >>> is_json('{"key": "value"}')
        True
        >>> is_json('invalid json')
        False
    """
    import json
    try:
        json.loads(json_string)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def is_number(value: Any) -> bool:
    """
    Checks if a value is a number (int, float, or numeric string).

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if the value is a number, False otherwise.

    Examples:
        >>> is_number(123)
        True
        >>> is_number('123.45')
        True
        >>> is_number('not a number')
        False
        >>> is_number(None)
        False
    """
    if isinstance(value, (int, float)):
        return True
    if isinstance(value, str) and value.strip():
        # Check if string can be converted to float
        try:
            float(value)
            return True
        except ValueError:
            return False
    return False