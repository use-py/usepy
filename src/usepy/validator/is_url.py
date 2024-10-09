def is_url(url: str) -> bool:
    """
    check if the given string is a valid URL.

    Args:
        url (str): the string to check.

    Returns:
        bool: if the string is a valid URL, return True, otherwise return False.

    Examples:
        >>> is_url("https://www.google.com")
        True
    """
    if not url or not isinstance(url, str):
        return False

    from urllib.parse import urlparse

    try:
        result = urlparse(url)
        if all([result.scheme, result.netloc]) and result.scheme in [
            "http",
            "https",
        ]:
            return True
    except ValueError:
        return False

    return False
