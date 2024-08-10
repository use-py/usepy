import random
from typing import TypeVar, Sequence

T = TypeVar('T')


def sample(arr: Sequence[T]) -> T:
    """
    Returns a random element from a sequence.

    This function takes a sequence (e.g., list, tuple) and returns a single element
    selected randomly from the sequence.

    Args:
        arr (Sequence[T]): The sequence to sample from.

    Returns:
        T: A random element from the sequence.

    Example:
        >>> sample([1, 2, 3, 4, 5])
        3
        >>> sample(('apple', 'banana', 'cherry'))
        'banana'
    """
    return random.choice(arr)
