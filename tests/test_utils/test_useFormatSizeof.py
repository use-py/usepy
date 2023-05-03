from usepy import useFormatSizeof


def test_useFormatSizeof():
    base_size = 1024
    suffix = "B"
    for i in range(1, 9):
        assert useFormatSizeof(base_size ** i) == f"1.0 {'_KMGTPEZY'[i]}{suffix}"
