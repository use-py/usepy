from typing import List, TypeVar, Sequence
import random

T = TypeVar('T')


def shuffle(arr: Sequence[T]) -> List[T]:
    """
    Randomizes the order of elements in a sequence using the Fisher-Yates algorithm.

    This function takes a sequence and returns a new list with its elements shuffled in a random order.

    Args:
        arr (Sequence[T]): The sequence to shuffle.

    Returns:
        List[T]: A new list with its elements shuffled in random order.

    Examples:
        >>> arr = [1, 2, 3, 4, 5]
        >>> shuffled_arr = shuffle(arr)
        >>> sorted(shuffled_arr) == sorted(arr)
        True
        >>> len(shuffled_arr) == len(arr)
        True
    """
    result = list(arr)
    random.shuffle(result)
    return result
