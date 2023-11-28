from usepy import useFuncName


def test_use_func_name():
    assert useFuncName() == "test_use_func_name"


class TestClass:
    def test_func(self):
        assert useFuncName() == "test_func"
        assert useFuncName(self) == "TestClass.test_func"
