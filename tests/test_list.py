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


@pytest.mark.parametrize(
    "lst, size, expected",
    [
        ([1, 2, 3, 4, 5], 2, [[1, 2], [3, 4], [5]]),
        ([1, 2, 3, 4, 5, 6], 3, [[1, 2, 3], [4, 5, 6]]),
    ],
)
def test_chunk(lst, size, expected):
    assert chunk(lst, size) == expected


@pytest.mark.parametrize(
    "lst, mapper, expected",
    [
        ([1, 2, 3, 4, 5], lambda x: x % 2 == 0, {True: 2, False: 3}),
        ([1, 2, 3, 4, 5, 6], lambda x: x % 3 == 0, {True: 2, False: 4}),
    ],
)
def test_count_by(lst, mapper, expected):
    assert count_by(lst, mapper) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([0, 1, False, 2, "", 3], [1, 2, 3]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_compact(lst, expected):
    assert compact(lst) == expected


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        ([2, 1], [2, 3], [1]),
        ([1, 2, 3, 4, 5], [2, 3, 4], [1, 5]),
    ],
)
def test_difference(lst1, lst2, expected):
    assert difference(lst1, lst2) == expected


@pytest.mark.parametrize(
    "lst, depth, expected",
    [
        ([1, [2, [3, [4]], 5]], 1, [1, 2, [3, [4]], 5]),
        ([1, [2, [3, [4]], 5]], 2, [1, 2, 3, [4], 5]),
        ([1, [2, [3, [4]], 5]], float("inf"), [1, 2, 3, 4, 5]),
    ],
)
def test_flatten(lst, depth, expected):
    assert flatten(lst, depth) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, [2, [3, [4]], 5]], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_flatten_deep(lst, expected):
    assert flatten_deep(lst) == expected


@pytest.mark.parametrize(
    "lst, fn, expected",
    [
        ([2, 4, 6], lambda x: x % 2 == 0, True),
        ([2, 3, 4], lambda x: x % 2 == 0, False),
    ],
)
def test_every(lst, fn, expected):
    assert every(lst, fn) == expected


@pytest.mark.parametrize(
    "lst, fn, expected",
    [
        ([1, 2, 3, 4], lambda x: x % 2 == 0, True),
        ([1, 3, 5, 7], lambda x: x % 2 == 0, False),
    ],
)
def test_some(lst, fn, expected):
    assert some(lst, fn) == expected


@pytest.mark.parametrize(
    "lst, n, expected",
    [
        ([1, 2, 3, 4, 5], 3, [1, 2, 3]),
        ([1, 2, 3, 4, 5], 2, [1, 2]),
    ],
)
def test_sample(lst, n, expected):
    sampled = sample(lst, n)
    assert len(sampled) == n
    assert all(item in lst for item in sampled)


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_shuffle(lst, expected):
    shuffled = shuffle(lst)
    assert sorted(shuffled) == expected


@pytest.mark.parametrize(
    "lst, items, expected",
    [
        ([2, 1, 2, 3], 1, [2, 2, 3]),
        ([2, 1, 2, 3], 2, [1, 3]),
    ],
)
def test_without(lst, items, expected):
    assert without(lst, items) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([2, 1, 2], [1, 2]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ],
)
def test_uniq(lst, expected):
    assert uniq(lst) == expected


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        ([2], [1, 2], [1, 2]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]),
    ],
)
def test_union(lst1, lst2, expected):
    assert union(lst1, lst2) == expected


@pytest.mark.parametrize(
    "lst, fn, expected",
    [
        (["a", "b", "c"], lambda x: x.upper(), {"A": "a", "B": "b", "C": "c"}),
        (["a", "b", "c"], lambda x: x.lower(), {"a": "a", "b": "b", "c": "c"}),
    ],
)
def test_key_by(lst, fn, expected):
    assert key_by(lst, fn) == expected


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        (["a", "b"], [1, 2], [("a", 1), ("b", 2)]),
        (["a", "b"], [1, 2, 3], [("a", 1), ("b", 2), (None, 3)]),
    ],
)
def test_zip_tuple(lst1, lst2, expected):
    assert zip_tuple(lst1, lst2) == expected


@pytest.mark.parametrize(
    "lst1, lst2, expected",
    [
        (["a", "b"], [1, 2], {"a": 1, "b": 2}),
        (["a", "b"], [1, 2, 3], {"a": 1, "b": 2}),
    ],
)
def test_zip_dict(lst1, lst2, expected):
    assert zip_dict(lst1, lst2) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3], 1),
        ([], None),
    ],
)
def test_first(lst, expected):
    assert first(lst) == expected


@pytest.mark.parametrize(
    "lst, expected",
    [
        ([1, 2, 3], 3),
        ([], None),
    ],
)
def test_last(lst, expected):
    assert last(lst) == expected
