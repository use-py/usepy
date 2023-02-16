from usepy import useString


def test_get_middle():
    assert useString.get_middle('abc123def', 'abc', 'def') == '123'
    assert useString.get_middle('abc123def', 'abc') == '123def'
    assert useString.get_middle('abc123def', end_str='def') == 'abc123'


def test_get_middle_batch():
    assert useString.get_middle_batch('abc123def456abc789def', 'abc', 'def') == ['123', '789']
    assert useString.get_middle_batch('abc123def456abc789def', 'abc', 'def', 1) == ['123']
    assert useString.get_middle_batch('abc123def456abc789def', end_str="def") == ['abc123', '456abc789']
    assert useString.get_middle_batch('abc123def456abc789def', start_str="abc") == ['123def456abc789def']


def test_get_left():
    assert useString.get_left('abc123def', 'def') == 'abc123'
    assert useString.get_left('abc123def', 'abc') == ''
    assert useString.get_left('abc123def', '123') == 'abc'


def test_get_right():
    assert useString.get_right('abc123def', 'abc') == '123def'
    assert useString.get_right('abc123def', 'def') == ''
    assert useString.get_right('abc123def', '123') == 'def'


def test_reverse():
    assert useString.reverse('') == ''
    assert useString.reverse('abc') == 'cba'
    assert useString.reverse('abc123') == '321cba'
    assert useString.reverse('abc123def') == 'fed321cba'


def test_uuid():
    assert useString.uuid() != useString.uuid()
    assert len(useString.uuid()) == 32


def test_to_str():
    assert useString.to_str(1) == '1'
    assert useString.to_str(1.1) == '1.1'
    assert useString.to_str(True) == 'True'
    assert useString.to_str(None) == 'None'
    assert useString.to_str([1, 2, 3]) == '[1, 2, 3]'
    assert useString.to_str({'a': 1, 'b': 2}) == "{'a': 1, 'b': 2}"
    assert useString.to_str(b'miclon') == "miclon"


def test_to_bytes():
    assert useString.to_bytes('miclon') == b'miclon'
    assert useString.to_bytes('miclon', encoding='utf-8') == b'miclon'
    assert useString.to_bytes('米乐', encoding='utf-8') == b'\xe7\xb1\xb3\xe4\xb9\x90'
    assert useString.to_bytes('米乐', encoding='gbk') == b'\xc3\xd7\xc0\xd6'
    assert useString.to_str(useString.to_bytes('米乐', encoding='gbk'), encoding='gbk') == '米乐'


def test_random():
    assert useString.random(10) != useString.random(10)
    assert len(useString.random(min_len=10, max_len=10)) == 10
    assert len(useString.random(max_len=3)) <= 3
    assert len(useString.random(min_len=30)) >= 30
