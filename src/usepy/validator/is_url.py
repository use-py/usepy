from urllib.parse import urlparse
from typing import List, Optional
import logging

logger = logging.getLogger(__name__)


def is_url(url: str, allowed_schemes: Optional[List[str]] = None) -> bool:
    """
    Check if the given string is a valid URL.

    Args:
        url (str): The string to check.
        allowed_schemes (Optional[List[str]]): List of allowed URL schemes.
            Defaults to ["http", "https"] if None.

    Returns:
        bool: If the string is a valid URL, return True, otherwise return False.

    Examples:
        >>> is_url("https://www.google.com")
        True
        >>> is_url("ftp://example.com", allowed_schemes=["ftp"])
        True
        >>> is_url("mailto:user@example.com", allowed_schemes=["mailto"])
        True
    """
    if not url or not isinstance(url, str):
        return False

    if allowed_schemes is None:
        allowed_schemes = ["http", "https"]

    try:
        result = urlparse(url)
        if result.scheme and result.scheme in allowed_schemes:
            return True
    except ValueError:
        logger.debug(f"Invalid URL format: {url}")
        return False

    return False
