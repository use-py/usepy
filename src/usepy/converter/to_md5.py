import hashlib
from typing import Any

from .to_string import to_string


def to_md5(data: Any) -> str:
    """Convert a value to a md5.

    Args:
        data (Any): The value to convert.

    Returns:
        str: The md5 value.

    Examples:
        >>> to_md5("hello")
        '5d41402abc4b2a76b9719d911017c592'
        >>> to_md5(b"hello")
        '5d41402abc4b2a76b9719d911017c592'
    """
    if isinstance(data, bytes):
        payload = data
    else:
        payload = to_string(data).encode("utf-8")

    return hashlib.md5(payload).hexdigest()
