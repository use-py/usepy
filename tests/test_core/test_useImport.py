from usepy import useImport


def test_import():
    module, _ = useImport("this")
    assert module.__name__ == "this"
    assert _ is None
