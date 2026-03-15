import pytest
from usepy.date import parse, format, now, timestamp, to_datetime
from datetime import datetime


@pytest.mark.parametrize(
    "date_string, expected",
    [
        ("2023-04-15 10:30:00", datetime(2023, 4, 15, 10, 30, 0)),
        ("2023-04-15", datetime(2023, 4, 15, 0, 0, 0)),
        ("2023-04-15 10:30", datetime(2023, 4, 15, 10, 30, 0)),
        ("2023-04-15 10:30:00", datetime(2023, 4, 15, 10, 30, 0)),
    ],
)
def test_parse(date_string, expected):
    parsed_date = parse(date_string)
    assert isinstance(parsed_date, datetime)
    assert parsed_date.year == expected.year
    assert parsed_date.month == expected.month
    assert parsed_date.day == expected.day
    assert parsed_date.hour == expected.hour
    assert parsed_date.minute == expected.minute
    assert parsed_date.second == expected.second
    assert parsed_date.microsecond == expected.microsecond
    assert parsed_date.tzinfo == expected.tzinfo


@pytest.mark.parametrize(
    "date, format_str, expected",
    [
        (datetime(2023, 4, 15, 10, 30, 0), "%Y-%m-%d %H:%M:%S", "2023-04-15 10:30:00"),
        (datetime(2023, 4, 15, 10, 30, 0), "%Y-%m-%d", "2023-04-15"),
        (datetime(2023, 4, 15, 10, 30, 0), "%Y-%m-%d %H:%M", "2023-04-15 10:30"),
        (datetime(2023, 4, 15, 10, 30, 0), "%Y-%m-%d %H:%M:%S", "2023-04-15 10:30:00"),
    ],
)
def test_format(date, format_str, expected):
    assert format(date, format_str) == expected


def test_now():
    current_time = now()
    assert isinstance(current_time, datetime)


class TestTimestamp:
    """Tests for timestamp() function"""

    def test_timestamp_default(self):
        """Test timestamp with default parameters (10 digits)"""
        dt = datetime(2023, 4, 15, 10, 30, 0)
        ts = timestamp(dt)
        assert isinstance(ts, int)
        assert len(str(ts)) == 10

    def test_timestamp_13_digits(self):
        """Test timestamp with 13 digits (milliseconds)"""
        dt = datetime(2023, 4, 15, 10, 30, 0)
        ts = timestamp(dt, digits=13)
        assert isinstance(ts, int)
        assert len(str(ts)) == 13

    def test_timestamp_no_datetime(self):
        """Test timestamp without providing datetime (uses current time)"""
        ts = timestamp()
        assert isinstance(ts, int)
        assert len(str(ts)) == 10

    def test_timestamp_invalid_digits(self):
        """Test timestamp with invalid digits raises ValueError"""
        dt = datetime(2023, 4, 15, 10, 30, 0)
        with pytest.raises(ValueError, match="timestamp digits must be 10 or 13"):
            timestamp(dt, digits=15)


class TestToDatetime:
    """Tests for to_datetime() function"""

    def test_to_datetime_10_digits(self):
        """Test converting 10-digit timestamp to datetime"""
        dt = datetime(2023, 4, 15, 10, 30, 0)
        ts = int(dt.timestamp())
        result = to_datetime(ts)
        assert isinstance(result, datetime)
        assert result.year == 2023
        assert result.month == 4
        assert result.day == 15

    def test_to_datetime_13_digits(self):
        """Test converting 13-digit timestamp (milliseconds) to datetime"""
        dt = datetime(2023, 4, 15, 10, 30, 0)
        ts = int(dt.timestamp() * 1000)
        result = to_datetime(ts)
        assert isinstance(result, datetime)
        assert result.year == 2023
        assert result.month == 4
        assert result.day == 15

    def test_to_datetime_invalid_digits(self):
        """Test to_datetime with invalid timestamp raises ValueError"""
        with pytest.raises(ValueError, match="timestamp digits must be 10 or 13"):
            to_datetime(123456789)  # 9 digits

    def test_timestamp_to_datetime_roundtrip(self):
        """Test roundtrip: datetime -> timestamp -> to_datetime"""
        original_dt = datetime(2023, 4, 15, 10, 30, 0)
        ts = timestamp(original_dt)
        result = to_datetime(ts)
        assert result.year == original_dt.year
        assert result.month == original_dt.month
        assert result.day == original_dt.day
        assert result.hour == original_dt.hour
        assert result.minute == original_dt.minute
        assert result.second == original_dt.second
