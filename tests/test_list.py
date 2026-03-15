import pytest
from usepy.list import (
    chunk,
    count_by,
    compact,
    difference,
    flatten,
    flatten_deep,
    every,
    some,
    sample,
    shuffle,
    without,
    uniq,
    union,
    key_by,
    zip_tuple,
    zip_dict,
    first,
    last,
)


class TestChunk:
    """Tests for chunk() function"""

    @pytest.mark.parametrize(
        "lst, size, expected",
        [
            ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
            ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
            ([], 2, []),
            ([1], 1, [[1]]),
            ([1, 2], 5, [[1, 2]]),
        ],
    )
    def test_chunk_normal(self, lst, size, expected):
        assert chunk(lst, size) == expected

    @pytest.mark.parametrize(
        "size",
        [0, -1, -10],
    )
    def test_chunk_invalid_size(self, size):
        """Test chunk with invalid size raises ValueError"""
        with pytest.raises(ValueError, match="Size must be an integer greater than zero"):
            chunk([1, 2, 3], size)

    def test_chunk_non_integer_size(self):
        """Test chunk with non-integer size raises ValueError"""
        with pytest.raises(ValueError, match="Size must be an integer greater than zero"):
            chunk([1, 2, 3], "2")


class TestCountBy:
    """Tests for count_by() function"""

    @pytest.mark.parametrize(
        "lst, mapper, expected",
        [
            ([1, 2, 3, 4, 5], lambda x: x % 2 == 0, {True: 2, False: 3}),
            ([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0, {True: 2, False: 4}),
            ([], lambda x: x, {}),
        ],
    )
    def test_count_by(self, lst, mapper, expected):
        assert count_by(lst, mapper) == expected


class TestCompact:
    """Tests for compact() function"""

    @pytest.mark.parametrize(
        "lst, expected",
        [
            ([0, 1, False, 2, "", 3], [1, 2, 3]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([None, 1, None, 2], [1, 2]),
            ([[], {}, 1, 2], [1, 2]),
            ([0, 0.0, False, None, "", [], {}], []),
            ([], []),
        ],
    )
    def test_compact(self, lst, expected):
        assert compact(lst) == expected


class TestDifference:
    """Tests for difference() function"""

    @pytest.mark.parametrize(
        "lst1, lst2, expected",
        [
            ([2, 1], [2, 3], [1]),
            ([1, 2, 3, 4, 5], [2, 3, 4], [1, 5]),
            ([], [1, 2], []),
            ([1, 2, 3], [], [1, 2, 3]),
            ([1, 1, 2, 2], [1], [2, 2]),
        ],
    )
    def test_difference(self, lst1, lst2, expected):
        assert difference(lst1, lst2) == expected


class TestFlatten:
    """Tests for flatten() function"""

    @pytest.mark.parametrize(
        "lst, depth, expected",
        [
            ([1, [2, [3, [4]], 5]], 1, [1, 2, [3, [4]], 5]),
            ([1, [2, [3, [4]], 5]], 2, [1, 2, 3, [4], 5]),
            ([1, [2, [3, [4]], 5]], float("inf"), [1, 2, 3, 4, 5]),
            ([], 1, []),
            ([1, 2, 3], 1, [1, 2, 3]),
        ],
    )
    def test_flatten(self, lst, depth, expected):
        assert flatten(lst, depth) == expected


class TestFlattenDeep:
    """Tests for flatten_deep() function"""

    @pytest.mark.parametrize(
        "lst, expected",
        [
            ([1, [2, [3, [4]], 5]], [1, 2, 3, 4, 5]),
            ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
            ([], []),
            ([[[[1]]]], [1]),
        ],
    )
    def test_flatten_deep(self, lst, expected):
        assert flatten_deep(lst) == expected


class TestEvery:
    """Tests for every() function"""

    @pytest.mark.parametrize(
        "lst, fn, expected",
        [
            ([2, 4, 6], lambda x: x % 2 == 0, True),
            ([2, 3, 4], lambda x: x % 2 == 0, False),
            ([], lambda x: x, True),  # empty list returns True
        ],
    )
    def test_every(self, lst, fn, expected):
        assert every(lst, fn) == expected


class TestSome:
    """Tests for some() function"""

    @pytest.mark.parametrize(
        "lst, fn, expected",
        [
            ([1, 2, 3, 4], lambda x: x % 2 == 0, True),
            ([1, 3, 5, 7], lambda x: x % 2 == 0, False),
            ([], lambda x: x, False),  # empty list returns False
        ],
    )
    def test_some(self, lst, fn, expected):
        assert some(lst, fn) == expected


class TestSample:
    """Tests for sample() function"""

    def test_sample_single_element(self):
        """Test sample returns single element when count=1 (default)"""
        lst = [1, 2, 3, 4, 5]
        result = sample(lst)
        assert result in lst

    def test_sample_multiple_elements(self):
        """Test sample returns list of correct length and valid elements"""
        lst = [1, 2, 3, 4, 5]
        n = 3
        sampled = sample(lst, n)
        assert len(sampled) == n
        assert all(item in lst for item in sampled)

    def test_sample_all_elements(self):
        """Test sample can return all elements"""
        lst = [1, 2, 3]
        sampled = sample(lst, 3)
        assert len(sampled) == 3
        assert set(sampled) == set(lst)


class TestShuffle:
    """Tests for shuffle() function"""

    def test_shuffle_preserves_elements(self):
        """Test shuffle returns same elements in different order"""
        lst = [1, 2, 3, 4, 5]
        shuffled = shuffle(lst)
        assert sorted(shuffled) == sorted(lst)

    def test_shuffle_single_element(self):
        """Test shuffle with single element"""
        assert shuffle([1]) == [1]

    def test_shuffle_empty_list(self):
        """Test shuffle with empty list"""
        assert shuffle([]) == []


class TestWithout:
    """Tests for without() function"""

    def test_without_single_value(self):
        """Test removing single value"""
        assert without([2, 1, 2, 3], 1) == [2, 2, 3]

    def test_without_multiple_values(self):
        """Test removing multiple values"""
        assert without([1, 2, 3, 4, 5], 2, 4) == [1, 3, 5]

    def test_without_no_match(self):
        """Test when value not in list"""
        assert without([1, 2, 3], 99) == [1, 2, 3]

    def test_without_empty_list(self):
        """Test with empty list"""
        assert without([], 1) == []


class TestUniq:
    """Tests for uniq() function"""

    @pytest.mark.parametrize(
        "lst, care_order, expected",
        [
            ([2, 1, 2], False, [1, 2]),
            ([1, 4, 1, 2, 5], True, [1, 4, 2, 5]),
            ([], True, []),
            ([1, 1, 1], True, [1]),
        ],
    )
    def test_uniq(self, lst, care_order, expected):
        assert uniq(lst, care_order) == expected

    def test_uniq_preserves_order(self):
        """Test uniq preserves order when care_order=True"""
        result = uniq([3, 1, 2, 1, 3], True)
        assert result == [3, 1, 2]


class TestUnion:
    """Tests for union() function"""

    @pytest.mark.parametrize(
        "lst1, lst2, expected",
        [
            ([2], [1, 2], [1, 2]),
            ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
            ([], [1, 2], [1, 2]),
            ([1, 2], [], [1, 2]),
        ],
    )
    def test_union(self, lst1, lst2, expected):
        assert union(lst1, lst2) == expected


class TestKeyBy:
    """Tests for key_by() function"""

    @pytest.mark.parametrize(
        "lst, fn, expected",
        [
            (["a", "b", "c"], lambda x: x.upper(), {"A": "a", "B": "b", "C": "c"}),
            (["a", "b", "c"], lambda x: x.lower(), {"a": "a", "b": "b", "c": "c"}),
            ([], lambda x: x, {}),
        ],
    )
    def test_key_by(self, lst, fn, expected):
        assert key_by(lst, fn) == expected


class TestZipTuple:
    """Tests for zip_tuple() function"""

    @pytest.mark.parametrize(
        "lst1, lst2, expected",
        [
            (["a", "b"], [1, 2], [("a", 1), ("b", 2)]),
            (["a", "b"], [1, 2, 3], [("a", 1), ("b", 2), (None, 3)]),
            ([], [], []),
            (["a"], [], [("a", None)]),
        ],
    )
    def test_zip_tuple(self, lst1, lst2, expected):
        assert zip_tuple(lst1, lst2) == expected


class TestZipDict:
    """Tests for zip_dict() function"""

    @pytest.mark.parametrize(
        "lst1, lst2, expected",
        [
            (["a", "b"], [1, 2], {"a": 1, "b": 2}),
            (["a", "b"], [1, 2, 3], {"a": 1, "b": 2}),
            ([], [], {}),
        ],
    )
    def test_zip_dict(self, lst1, lst2, expected):
        assert zip_dict(lst1, lst2) == expected


class TestFirst:
    """Tests for first() function"""

    @pytest.mark.parametrize(
        "lst, expected",
        [
            ([1, 2, 3], 1),
            ([], None),
            (["a", "b", "c"], "a"),
        ],
    )
    def test_first(self, lst, expected):
        assert first(lst) == expected


class TestLast:
    """Tests for last() function"""

    @pytest.mark.parametrize(
        "lst, expected",
        [
            ([1, 2, 3], 3),
            ([], None),
            (["a", "b", "c"], "c"),
        ],
    )
    def test_last(self, lst, expected):
        assert last(lst) == expected