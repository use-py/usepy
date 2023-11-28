from usepy import useAdDict

test_dict = {
    "title": "test",
    "detail": {"authors": ["author1", "author2"], "content": "test content"},
}

if __name__ == "__main__":
    d = useAdDict(test_dict)
    assert d.title == "test"
    assert d.detail.authors[0] == "author1"
    assert d.test == {}
