from typing import List, TypeVar, Sequence

T = TypeVar('T')


def uniq(lst: Sequence[T], care_order: bool = True) -> List[T]:
    """
    Returns a new list containing only the unique elements from the input sequence.

    Args:
        lst (Sequence[T]): The input sequence.

    Returns:
        List[T]: A new list containing only the unique elements from the input sequence.

    Example:
        >>> uniq([1, 2, 3, 2, 1])
        [1, 2, 3]
    """
    if care_order:
        seen = set()
        result = []
        for item in lst:
            if item not in seen:
                seen.add(item)
                result.append(item)
        return result
    else:
        return list(set(lst))
