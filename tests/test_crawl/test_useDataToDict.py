from usepy import useDataToDict


def test_data_to_dict():
    data_str = "key1=value1&key2=value2"
    assert useDataToDict(data_str) == {
        "key1": "value1",
        "key2": "value2",
    }
