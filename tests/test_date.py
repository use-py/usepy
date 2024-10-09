import pytest
from usepy.date import parse, format, now
from datetime import datetime, timezone


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
