from usepy.data import useAdDict, useList, useString

if __name__ == '__main__':
    assert list(
        useList.split([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    ) == [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    assert useList.objs_to_obj(
        [{'id': 1, 'name': 'miclon'}, {'id': 2, 'name': 'miclon2'}], 'id'
    ) == {1: {'id': 1, 'name': 'miclon'}, 2: {'id': 2, 'name': 'miclon2'}}

    d = useAdDict({'a': 1, 'b': 2, 'c': {'d': 3, 'e': 4}})
    assert d.a == 1
    assert d.c.e == 4

    assert useString.get_middle('abc', 'a', 'c') == 'b'

    print(useString.encode('xxxx', '12345678'))
