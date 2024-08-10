from typing import TypeVar
import re

T = TypeVar('T', bound=str)

CASE_SPLIT_PATTERN = re.compile(r'[A-Z]?[a-z]+|[0-9]+|[A-Z]+(?![a-z])', re.VERBOSE)


def get_words(string: T) -> list[T]:
    """
    Splits a string into words based on whitespace and non-alphanumeric characters.

    Args:
        string (str): The input string to be split into words.

    Returns:
        list[str]: A list of words extracted from the input string.

    Example:
        >>> get_words('hello world')
        ['hello', 'world']
        >>> get_words('hello-world/foo_bar')
        ['hello', 'world', 'foo', 'bar']
    """
    return re.findall(CASE_SPLIT_PATTERN, string)
