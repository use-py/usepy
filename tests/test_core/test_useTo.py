from usepy import useToBytes, useToCamel, useToMD5, useToSHA1, useToSnake, useToString


def test_to_str():
    assert useToString(1) == "1"
    assert useToString(1.1) == "1.1"
    assert useToString(True) == "True"
    assert useToString(None) == "None"
    assert useToString([1, 2, 3]) == "[1, 2, 3]"
    assert useToString({"a": 1, "b": 2}) == "{'a': 1, 'b': 2}"
    assert useToString(b"miclon") == "miclon"


def test_to_bytes():
    assert useToBytes("miclon") == b"miclon"
    assert useToBytes("miclon", encoding="utf-8") == b"miclon"
    assert useToBytes("米乐", encoding="utf-8") == b"\xe7\xb1\xb3\xe4\xb9\x90"
    assert useToBytes("米乐", encoding="gbk") == b"\xc3\xd7\xc0\xd6"
    assert useToString(useToBytes("米乐", encoding="gbk"), encoding="gbk") == "米乐"


def test_to_md5():
    assert useToMD5("qq1234") == "4547e2781bd1d816166766fda702c7d9"


def test_to_sha1():
    assert useToSHA1("qq1234") == "ada62457359ea34588fd316b33fbd24e8296d577"


def test_to_camel():
    assert useToCamel("test") == "test"
    assert useToCamel("test-case") == "testCase"
    assert useToCamel("test_case", char="_") == "testCase"


def test_to_snake():
    assert useToSnake("test") == "test"
    assert useToSnake("testCase") == "test_case"
    assert useToSnake("testCase", char="-") == "test-case"
