import pytest
from usepy.dict import AdDict, sort_by_key, sort_by_value, merge_dicts


def test_ad_dict():
    ad = AdDict()
    ad.a = 1
    ad["b"] = 2

    assert ad.a == 1
    assert ad["b"] == 2
    assert ad.get("c", 3) == 3


def test_sort_by_key():
    d = {"c": 3, "a": 1, "b": 2}
    sorted_d = sort_by_key(d)
    assert list(sorted_d.keys()) == ["a", "b", "c"]
    assert list(sorted_d.values()) == [1, 2, 3]


def test_sort_by_value():
    d = {"c": 3, "a": 1, "b": 2}
    sorted_d = sort_by_value(d)
    assert list(sorted_d.keys()) == ["a", "b", "c"]
    assert list(sorted_d.values()) == [1, 2, 3]


def test_merge_dicts():
    d1 = {"a": 1, "b": 2}
    d2 = {"b": 3, "c": 4}
    merged = merge_dicts(d1, d2)
    assert merged == {"a": 1, "b": 3, "c": 4}

    # Test with more than two dictionaries
    d3 = {"d": 5}
    merged = merge_dicts(d1, d2, d3)
    assert merged == {"a": 1, "b": 3, "c": 4, "d": 5}
