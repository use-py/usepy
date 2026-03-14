import pytest
from usepy.string import (
    trim, trim_start, trim_end,
    truncate,
    starts_with, ends_with,
    repeat,
    pad_start, pad_end,
)


class TestTrim:
    """Tests for trim functions"""

    def test_trim_spaces(self):
        """Test trimming spaces"""
        assert trim('  hello  ') == 'hello'

    def test_trim_chars(self):
        """Test trimming specific chars"""
        assert trim('xxhelloxx', 'x') == 'hello'

    def test_trim_newline_tab(self):
        """Test trimming newline and tab"""
        assert trim('\n\thello\n', None) == 'hello'

    def test_trim_start(self):
        """Test trimming start only"""
        assert trim_start('  hello  ') == 'hello  '
        assert trim_start('xxhelloxx', 'x') == 'helloxx'

    def test_trim_end(self):
        """Test trimming end only"""
        assert trim_end('  hello  ') == '  hello'
        assert trim_end('xxhelloxx', 'x') == 'xxhello'


class TestTruncate:
    """Tests for truncate() function"""

    def test_truncate_long(self):
        """Test truncating long string"""
        assert truncate('hello world this is a long string', 15) == 'hello world ...'

    def test_truncate_short(self):
        """Test not truncating short string"""
        assert truncate('short', 10) == 'short'

    def test_truncate_custom_omission(self):
        """Test with custom omission"""
        assert truncate('hello world', 8, omission='~') == 'hello w~'

    def test_truncate_exact_length(self):
        """Test string at exact length"""
        assert truncate('hello', 5) == 'hello'

    def test_truncate_zero_length(self):
        """Test with very small length"""
        assert truncate('hello', 2) == '..'


class TestStartsEndsWith:
    """Tests for starts_with() and ends_with() functions"""

    def test_starts_with_true(self):
        """Test starts_with returns True"""
        assert starts_with('hello world', 'hello') is True

    def test_starts_with_false(self):
        """Test starts_with returns False"""
        assert starts_with('hello world', 'world') is False

    def test_starts_with_empty(self):
        """Test starts_with with empty prefix"""
        assert starts_with('hello', '') is True

    def test_ends_with_true(self):
        """Test ends_with returns True"""
        assert ends_with('hello world', 'world') is True

    def test_ends_with_false(self):
        """Test ends_with returns False"""
        assert ends_with('hello world', 'hello') is False

    def test_ends_with_empty(self):
        """Test ends_with with empty suffix"""
        assert ends_with('hello', '') is True


class TestRepeat:
    """Tests for repeat() function"""

    def test_repeat_normal(self):
        """Test repeating string"""
        assert repeat('abc', 3) == 'abcabcabc'

    def test_repeat_zero(self):
        """Test repeating zero times"""
        assert repeat('x', 0) == ''

    def test_repeat_empty(self):
        """Test repeating empty string"""
        assert repeat('', 5) == ''

    def test_repeat_one(self):
        """Test repeating once"""
        assert repeat('x', 1) == 'x'


class TestPad:
    """Tests for pad_start() and pad_end() functions"""

    def test_pad_start_default(self):
        """Test pad_start with default pad"""
        assert pad_start('abc', 5) == '  abc'

    def test_pad_start_custom(self):
        """Test pad_start with custom pad"""
        assert pad_start('abc', 6, 'x') == 'xxxabc'

    def test_pad_start_shorter(self):
        """Test pad_start when string already longer"""
        assert pad_start('abc', 2) == 'abc'

    def test_pad_end_default(self):
        """Test pad_end with default pad"""
        assert pad_end('abc', 5) == 'abc  '

    def test_pad_end_custom(self):
        """Test pad_end with custom pad"""
        assert pad_end('abc', 6, 'x') == 'abcxxx'

    def test_pad_end_shorter(self):
        """Test pad_end when string already longer"""
        assert pad_end('abc', 2) == 'abc'

    def test_pad_multichar(self):
        """Test pad with multi-char string"""
        assert pad_start('a', 5, 'ab') == 'ababa'
        assert pad_end('a', 5, 'ab') == 'aabab'