from typing import TypeVar, Dict, Hashable

K = TypeVar('K', bound=Hashable)
V = TypeVar('V', bound=Hashable)


def invert(d: Dict[K, V]) -> Dict[V, K]:
    """
    Creates a new dictionary with keys and values swapped.

    If there are duplicate values, the last key wins.

    Args:
        d (Dict[K, V]): The source dictionary.

    Returns:
        Dict[V, K]: A new dictionary with keys and values swapped.

    Examples:
        >>> invert({'a': 1, 'b': 2})
        {1: 'a', 2: 'b'}
        >>> invert({'a': 1, 'b': 1})
        {1: 'b'}
    """
    return {v: k for k, v in d.items()}