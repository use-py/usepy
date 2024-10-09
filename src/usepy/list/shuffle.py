from typing import TypeVar, Sequence
import random

T = TypeVar('T')


def shuffle(arr: Sequence[T]) -> list[T]:
    """
    Randomizes the order of elements in a sequence using the Fisher-Yates algorithm.

    This function takes a sequence and returns a new list with its elements shuffled in a random order.

    Args:
        arr (Sequence[T]): The sequence to shuffle.

    Returns:
        list[T]: A new list with its elements shuffled in random order.

    Examples:
        >>> arr = [1, 2, 3, 4, 5]
        >>> shuffled_arr = shuffle(arr)
        >>> sorted(shuffled_arr) == sorted(arr)
        True
        >>> len(shuffled_arr) == len(arr)
        True
    """
    result = list(arr)

    for i in range(len(result) - 1, 0, -1):
        j = random.randint(0, i)
        result[i], result[j] = result[j], result[i]

    return result
