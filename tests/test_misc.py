import pytest
from usepy.misc import get_function_name, dynamic_import


def test_get_function_name():

    assert get_function_name() == "test_get_function_name"


def test_dynamic_import():
    module, function = dynamic_import("usepy.list.chunk")
    assert function.__name__ == "chunk"
    assert module.__name__ == "usepy.list"

    with pytest.raises(ImportError):
        dynamic_import("non_existent_module")

    module, _ = dynamic_import("json")
    assert (
        module.loads(
            """
        {"a": 1, "b": 2}
        """
        )
        == {"a": 1, "b": 2}
    )
