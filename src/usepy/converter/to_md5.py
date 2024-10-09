from typing import AnyStr
from .to_string import to_string


def to_md5(data: AnyStr) -> str:
    """Convert a value to a md5.

    Args:
        value (AnyStr): The value to convert.

    Returns:
        str: The md5 value.

    Examples:
        >>> to_md5("hello")
        '5d41402abc4b2a76b9719d911017c592'
    """
    import hashlib

    return hashlib.md5(to_string(data).encode()).hexdigest()
