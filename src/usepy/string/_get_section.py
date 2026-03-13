from typing import Optional, Tuple


def get_section(
        original_str: str, start_str: Optional[str] = None, end_str: Optional[str] = None
) -> Tuple[Optional[str], Optional[int], Optional[int]]:
    """
    Get the substring between two given substrings in a string.

    Args:
        original_str (str): The original string to search in.
        start_str (Optional[str], optional): The substring to start the search from.
            If not provided, the search starts from the beginning of the string.
        end_str (Optional[str], optional): The substring to end the search at.
            If not provided, the search ends at the end of the string.

    Returns:
        Tuple[Optional[str], Optional[int], Optional[int]]:
            - The substring between the start and end substrings, or None if not found.
            - The starting index of the substring, or None if not found.
            - The ending index of the substring, or None if not found.

    Examples:
        >>> get_section('abc123def', 'abc', 'def')
        ('123', 3, 6)
        >>> get_section('abc123def', 'abc')
        ('123def', 3, 9)
        >>> get_section('abc123def', end_str='def')[0]
        'abc123'
    """
    if start_str is None:
        start_index = 0
    else:
        start_index = original_str.find(start_str)
        if start_index >= 0:
            start_index += len(start_str)
        else:
            return None, start_index, None

    if end_str is None:
        end_index = len(original_str)
    else:
        end_index = original_str.find(end_str, start_index)

    if end_index >= 0:
        return original_str[start_index:end_index], start_index, end_index

    return None, None, None
