from typing import TypeVar, Sequence, Set

T = TypeVar('T')


def difference(first_lst: Sequence[T], second_lst: Sequence[T]) -> list[T]:
    """
    Computes the difference between two sequences.

    This function takes two sequences and returns a new sequence containing the elements
    that are present in the first sequence but not in the second sequence. It effectively
    filters out any elements from the first sequence that also appear in the second sequence.

    Args:
        first_lst (Sequence[T]): The sequence from which to derive the difference. This is the primary sequence
        from which elements will be compared and filtered.
        second_lst (Sequence[T]): The sequence containing elements to be excluded from the first sequence.
        Each element in this sequence will be checked against the first sequence, and if a match is found,
        that element will be excluded from the result.

    Returns:
        list[T]: A new sequence containing the elements that are present in the first sequence but not
        in the second sequence.

    Example:
        >>> array1 = [1, 2, 3, 4, 5]
        >>> array2 = [2, 4]
        >>> result = difference(array1,array2)
        >>> result
        [1, 3, 5]
    """
    second_set: Set[T] = set(second_lst)
    return [item for item in first_lst if item not in second_set]
