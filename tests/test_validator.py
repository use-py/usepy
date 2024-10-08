import pytest
import asyncio
from usepy.validator import is_async_function, is_url


def test_is_async_function():
    async def async_func():
        pass

    def sync_func():
        pass

    assert is_async_function(async_func)
    assert not is_async_function(sync_func)


def test_is_url():
    assert is_url("https://www.example.com")
    assert is_url("http://localhost:8000")
    assert not is_url("not a url")
    assert not is_url("mailto:user@example.com")
    assert not is_url("ftp://invalid-scheme.com")
