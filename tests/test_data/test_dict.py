from usepy.data import useAdDict, useList, useString, useDict


def test_use_addict():
    test_dict = {'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}}
    d = useAdDict(test_dict)
    assert d.a == 1
    assert d.c.e == 4
    d.q.q = 100
    assert d.q.q == 100


def test_use_list():
    ul = useList()
    assert list(ul.split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    assert ul.objs_to_obj(
        [{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id') == {1: {'id': 1, 'name': 'miclon'},
                                                                               2: {'id': 2, 'name': 'miclon2'}}
    assert list(useList.dedupe([1, 5, 2, 1, 9, 1, 5, 10])) == [1, 5, 2, 9, 10]


def test_use_dict():
    assert useDict.find_keys({'a': 1, 'b': 2, 'c': 3}, 2) == ['b']
    assert useDict.reverse({'a': 1, 'b': 2, 'c': 3}) == {1: 'a', 2: 'b', 3: 'c'}
    assert useDict.sort_by_key({'c': 1, 'b': 2, 'a': 3}) == {'a': 3, 'b': 2, 'c': 1}
    assert useDict.sort_by_value({'c': 1, 'b': 2, 'a': 3}) == {'c': 1, 'b': 2, 'a': 3}

    assert useDict.arrays_to_dict(['a', 'b', 'c'], [1, 2, 3]) == {'a': 1, 'b': 2, 'c': 3}


def test_merge():
    assert useDict.merge({'a': 1, 'b': 2}, {'c': 3, 'd': 4}) == {'a': 1, 'b': 2, 'c': 3, 'd': 4}

    assert useDict.merge_values({'a': 1, 'b': 2}, {'a': 3, 'b': 4}) == {'a': [1, 3], 'b': [2, 4]}
