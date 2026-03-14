from typing import TypeVar, Sequence, Callable, Tuple, List

T = TypeVar('T')


def partition(arr: Sequence[T], predicate: Callable[[T], bool]) -> Tuple[List[T], List[T]]:
    """
    Partitions a sequence into two lists based on a predicate function.

    Args:
        arr (Sequence[T]): The sequence to partition.
        predicate (Callable[[T], bool]): A function that returns True for elements to be in the first list.

    Returns:
        Tuple[List[T], List[T]]: A tuple of two lists - elements that satisfy the predicate and those that don't.

    Examples:
        >>> partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        ([2, 4], [1, 3, 5])
        >>> partition(['a', 'bb', 'ccc'], lambda x: len(x) > 1)
        (['bb', 'ccc'], ['a'])
        >>> partition([], lambda x: x > 0)
        ([], [])
    """
    matches: List[T] = []
    rest: List[T] = []

    for item in arr:
        if predicate(item):
            matches.append(item)
        else:
            rest.append(item)

    return matches, rest