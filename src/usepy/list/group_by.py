from typing import TypeVar, Sequence, Callable, Dict, List

T = TypeVar('T')
K = TypeVar('K')


def group_by(arr: Sequence[T], key_func: Callable[[T], K]) -> Dict[K, List[T]]:
    """
    Groups elements of a sequence by a key generated from a function.

    Args:
        arr (Sequence[T]): The sequence to group.
        key_func (Callable[[T], K]): A function that generates a key from each element.

    Returns:
        Dict[K, List[T]]: A dictionary where keys are the generated keys and values are lists of elements.

    Examples:
        >>> group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4]}
        >>> group_by(['apple', 'banana', 'apricot'], lambda x: x[0])
        {'a': ['apple', 'apricot'], 'b': ['banana']}
    """
    result: Dict[K, List[T]] = {}
    for item in arr:
        key = key_func(item)
        if key not in result:
            result[key] = []
        result[key].append(item)
    return result