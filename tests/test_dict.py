import pytest
from usepy.dict import AdDict, sort_by_key, sort_by_value, merge_dicts


def test_ad_dict():
    ad = AdDict()
    ad.a = 1
    ad["b"] = 2

    assert ad.a == 1
    assert ad["b"] == 2
    assert ad.get("c", 3) == 3


@pytest.mark.parametrize(
    "input, az, expected",
    [
        ({"c": 3, "a": 1, "b": 2}, True, ["a", "b", "c"]),
        ({"a": 1, "b": 2, "c": 3}, False, ["c", "b", "a"]),
    ],
)
def test_sort_by_key(input, az, expected):
    sorted_d = sort_by_key(input, az)
    assert list(sorted_d.keys()) == expected


@pytest.mark.parametrize(
    "input, az, expected",
    [
        ({"c": 3, "a": 1, "b": 2}, True, ["a", "b", "c"]),
        ({"a": 1, "b": 2, "c": 3}, False, ["c", "b", "a"]),
    ],
)
def test_sort_by_value(input, az, expected):
    sorted_d = sort_by_value(input, az)
    assert list(sorted_d.keys()) == expected


@pytest.mark.parametrize(
    "dict1, dict2, expected",
    [
        ({"a": 1, "b": 2}, {"b": 3, "c": 4}, {"a": 1, "b": 3, "c": 4}),
        ({"a": 1, "b": 2}, {"b": 3, "c": 4, "d": 5}, {"a": 1, "b": 3, "c": 4, "d": 5}),
    ],
)
def test_merge_dicts(dict1, dict2, expected):
    merged = merge_dicts(dict1, dict2)
    assert merged == expected
