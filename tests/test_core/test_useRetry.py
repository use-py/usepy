import pytest

from usepy import useRetry
from usepy.core.useRetry import MaxRetryError


@useRetry(max_retry=3, retry_interval=1)
def my_func():
    print(1 / 0)  # error always


def test_useRetry():
    with pytest.raises(MaxRetryError):
        my_func()
