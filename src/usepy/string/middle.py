from typing import Optional


def middle(
        original_str: str, start_str: Optional[str] = None, end_str: Optional[str] = None
) -> Optional[str]:
    """
    Get the substring between two given substrings in a string.

    Args:
        original_str (str): The original string to search in.
        start_str (Optional[str], optional): The substring to start the search from.
            If not provided, the search starts from the beginning of the string.
        end_str (Optional[str], optional): The substring to end the search at.
            If not provided, the search ends at the end of the string.

    Returns:
        Optional[str]: The substring between the start and end substrings, or None if not found.

    Examples:
        >>> middle('abc123def', 'abc', 'def')
        '123'
    """
    from usepy.string._get_section import get_section

    result, _, _ = get_section(original_str, start_str, end_str)
    return result
