import pytest
from usepy.validator import is_async_function, is_url


class TestIsAsyncFunction:
    """Tests for is_async_function()"""

    def test_async_function(self):
        """Test is_async_function returns True for async function"""

        async def async_func():
            pass

        assert is_async_function(async_func) is True

    def test_sync_function(self):
        """Test is_async_function returns False for sync function"""

        def sync_func():
            pass

        assert is_async_function(sync_func) is False

    def test_lambda(self):
        """Test is_async_function returns False for lambda"""
        assert is_async_function(lambda x: x) is False

    def test_class_method(self):
        """Test is_async_function with class methods"""

        class TestClass:
            async def async_method(self):
                pass

            def sync_method(self):
                pass

        assert is_async_function(TestClass.async_method) is True
        assert is_async_function(TestClass.sync_method) is False


class TestIsUrl:
    """Tests for is_url()"""

    def test_valid_http_url(self):
        """Test is_url returns True for valid HTTP URL"""
        assert is_url("http://example.com") is True

    def test_valid_https_url(self):
        """Test is_url returns True for valid HTTPS URL"""
        assert is_url("https://www.example.com") is True

    def test_valid_localhost_url(self):
        """Test is_url returns True for localhost URL"""
        assert is_url("http://localhost:8000") is True

    def test_invalid_url(self):
        """Test is_url returns False for invalid URL"""
        assert is_url("not a url") is False

    def test_empty_string(self):
        """Test is_url returns False for empty string"""
        assert is_url("") is False

    def test_none_input(self):
        """Test is_url returns False for None"""
        assert is_url(None) is False

    def test_non_string_input(self):
        """Test is_url returns False for non-string types"""
        assert is_url(123) is False
        assert is_url([]) is False
        assert is_url({}) is False

    def test_url_with_custom_scheme(self):
        """Test is_url with custom allowed schemes"""
        assert is_url("mailto:user@example.com", allowed_schemes=["mailto"]) is True
        assert is_url("ftp://files.example.com", allowed_schemes=["ftp"]) is True

    def test_url_scheme_not_allowed(self):
        """Test is_url returns False when scheme not in allowed list"""
        assert is_url("ftp://files.example.com") is False  # default is http/https
        assert is_url("mailto:user@example.com") is False

    def test_url_without_scheme(self):
        """Test is_url returns False for URL without scheme"""
        assert is_url("example.com") is False
        assert is_url("www.example.com") is False

    def test_url_with_path(self):
        """Test is_url returns True for URL with path"""
        assert is_url("https://example.com/path/to/page") is True

    def test_url_with_query(self):
        """Test is_url returns True for URL with query string"""
        assert is_url("https://example.com/search?q=test") is True