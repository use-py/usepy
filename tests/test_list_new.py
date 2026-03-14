import pytest
from usepy.list import (
    group_by,
    find,
    find_index,
    intersection,
    partition,
    take,
    take_right,
    drop,
    drop_right,
    nth,
)


class TestGroupBy:
    """Tests for group_by() function"""

    def test_group_by_even_odd(self):
        """Test grouping by even/odd"""
        result = group_by([1, 2, 3, 4, 5], lambda x: x % 2)
        assert result == {1: [1, 3, 5], 0: [2, 4]}

    def test_group_by_first_letter(self):
        """Test grouping by first letter"""
        result = group_by(['apple', 'banana', 'apricot', 'blueberry'], lambda x: x[0])
        assert result == {'a': ['apple', 'apricot'], 'b': ['banana', 'blueberry']}

    def test_group_by_empty(self):
        """Test grouping empty list"""
        assert group_by([], lambda x: x) == {}

    def test_group_by_length(self):
        """Test grouping by string length"""
        result = group_by(['a', 'bb', 'c', 'dd'], len)
        assert result == {1: ['a', 'c'], 2: ['bb', 'dd']}


class TestFind:
    """Tests for find() function"""

    def test_find_element(self):
        """Test finding an element"""
        assert find([1, 2, 3, 4], lambda x: x > 2) == 3

    def test_find_not_found(self):
        """Test element not found returns None"""
        assert find([1, 2, 3], lambda x: x > 10) is None

    def test_find_with_default(self):
        """Test element not found returns default"""
        assert find([1, 2, 3], lambda x: x > 10, default=0) == 0

    def test_find_empty(self):
        """Test finding in empty list"""
        assert find([], lambda x: x > 0) is None

    def test_find_first_match(self):
        """Test returns first matching element"""
        assert find([1, 2, 3, 4, 5], lambda x: x > 2) == 3


class TestFindIndex:
    """Tests for find_index() function"""

    def test_find_index(self):
        """Test finding index"""
        assert find_index([1, 2, 3, 4], lambda x: x > 2) == 2

    def test_find_index_not_found(self):
        """Test index not found returns -1"""
        assert find_index([1, 2, 3], lambda x: x > 10) == -1

    def test_find_index_empty(self):
        """Test finding index in empty list"""
        assert find_index([], lambda x: x > 0) == -1

    def test_find_index_first_match(self):
        """Test returns first matching index"""
        assert find_index([1, 2, 3, 2, 1], lambda x: x == 2) == 1


class TestIntersection:
    """Tests for intersection() function"""

    def test_intersection_two_arrays(self):
        """Test intersection of two arrays"""
        assert intersection([1, 2, 3], [2, 3, 4]) == [2, 3]

    def test_intersection_three_arrays(self):
        """Test intersection of three arrays"""
        assert intersection([1, 2, 3], [2, 3, 4], [2, 3, 5]) == [2, 3]

    def test_intersection_no_common(self):
        """Test no common elements"""
        assert intersection([1, 2, 3], [4, 5, 6]) == []

    def test_intersection_empty(self):
        """Test intersection with empty"""
        assert intersection([], [1, 2]) == []
        assert intersection([1, 2], []) == []

    def test_intersection_duplicates(self):
        """Test intersection preserves first array order without duplicates"""
        assert intersection([1, 2, 2, 3], [2, 3]) == [2, 3]


class TestPartition:
    """Tests for partition() function"""

    def test_partition_even_odd(self):
        """Test partitioning by even/odd"""
        matches, rest = partition([1, 2, 3, 4, 5], lambda x: x % 2 == 0)
        assert matches == [2, 4]
        assert rest == [1, 3, 5]

    def test_partition_all_match(self):
        """Test all elements match"""
        matches, rest = partition([2, 4, 6], lambda x: x % 2 == 0)
        assert matches == [2, 4, 6]
        assert rest == []

    def test_partition_none_match(self):
        """Test no elements match"""
        matches, rest = partition([1, 3, 5], lambda x: x % 2 == 0)
        assert matches == []
        assert rest == [1, 3, 5]

    def test_partition_empty(self):
        """Test partitioning empty list"""
        matches, rest = partition([], lambda x: x > 0)
        assert matches == []
        assert rest == []


class TestTake:
    """Tests for take() and take_right() functions"""

    def test_take(self):
        """Test taking first n elements"""
        assert take([1, 2, 3, 4, 5], 2) == [1, 2]

    def test_take_zero(self):
        """Test taking zero elements"""
        assert take([1, 2, 3], 0) == []

    def test_take_more_than_length(self):
        """Test taking more than length"""
        assert take([1, 2, 3], 10) == [1, 2, 3]

    def test_take_default(self):
        """Test taking with default n=1"""
        assert take([1, 2, 3]) == [1]

    def test_take_right(self):
        """Test taking last n elements"""
        assert take_right([1, 2, 3, 4, 5], 2) == [4, 5]

    def test_take_right_zero(self):
        """Test taking zero elements from right"""
        assert take_right([1, 2, 3], 0) == []

    def test_take_right_more_than_length(self):
        """Test taking more than length from right"""
        assert take_right([1, 2, 3], 10) == [1, 2, 3]


class TestDrop:
    """Tests for drop() and drop_right() functions"""

    def test_drop(self):
        """Test dropping first n elements"""
        assert drop([1, 2, 3, 4, 5], 2) == [3, 4, 5]

    def test_drop_zero(self):
        """Test dropping zero elements"""
        assert drop([1, 2, 3], 0) == [1, 2, 3]

    def test_drop_more_than_length(self):
        """Test dropping more than length"""
        assert drop([1, 2, 3], 10) == []

    def test_drop_default(self):
        """Test dropping with default n=1"""
        assert drop([1, 2, 3]) == [2, 3]

    def test_drop_right(self):
        """Test dropping last n elements"""
        assert drop_right([1, 2, 3, 4, 5], 2) == [1, 2, 3]

    def test_drop_right_zero(self):
        """Test dropping zero elements from right"""
        assert drop_right([1, 2, 3], 0) == [1, 2, 3]

    def test_drop_right_more_than_length(self):
        """Test dropping more than length from right"""
        assert drop_right([1, 2, 3], 10) == []


class TestNth:
    """Tests for nth() function"""

    def test_nth_positive(self):
        """Test getting nth element (positive index)"""
        assert nth([1, 2, 3, 4, 5], 1) == 2

    def test_nth_negative(self):
        """Test getting nth element (negative index)"""
        assert nth([1, 2, 3, 4, 5], -1) == 5
        assert nth([1, 2, 3, 4, 5], -2) == 4

    def test_nth_out_of_bounds(self):
        """Test out of bounds returns default"""
        assert nth([1, 2, 3], 10) is None
        assert nth([1, 2, 3], 10, default=0) == 0

    def test_nth_empty(self):
        """Test getting nth from empty list"""
        assert nth([], 0) is None

    def test_nth_first(self):
        """Test getting first element"""
        assert nth([1, 2, 3], 0) == 1