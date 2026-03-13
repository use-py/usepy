from typing import TypeVar, Sequence, List

T = TypeVar('T')


def chunk(arr: Sequence[T], size: int) -> List[List[T]]:
    """
    Splits a sequence into smaller sequences of a specified length.

    This function takes an input sequence and divides it into multiple smaller sequences,
    each of a specified length. If the input sequence cannot be evenly divided,
    the final sub-sequence will contain the remaining elements.

    Args:
        arr (Sequence[T]): The sequence to be chunked into smaller sequences.
        size (int): The size of each smaller sequence. Must be a positive integer.

    Returns:
        List[List[T]]: A two-dimensional list where each sub-list has a maximum length of `size`.

    Raises:
        ValueError: If `size` is not a positive integer.

    Examples:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]

        >>> chunk(['a', 'b', 'c', 'd', 'e', 'f', 'g'], 3)
        [['a', 'b', 'c'], ['d', 'e', 'f'], ['g']]
    """
    if not isinstance(size, int) or size <= 0:
        raise ValueError('Size must be an integer greater than zero.')

    chunk_length = (len(arr) + size - 1) // size
    result: List[List[T]] = [[] for _ in range(chunk_length)]

    for i, item in enumerate(arr):
        result[i // size].append(item)

    return result
