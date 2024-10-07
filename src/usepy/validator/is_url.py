import re


def is_url(url: str) -> bool:
    """
    Check if the given string is a valid URL.

    Args:
        url (str): The string to check.

    Returns:
        bool: True if the string is a valid URL, False otherwise.

    Examples:
        >>> is_url("https://www.google.com")
        True
    """
    pattern = re.compile(
        r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$"
    )
    return bool(pattern.match(url))
