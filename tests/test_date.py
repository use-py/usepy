import pytest
from usepy.date import parse, format, now
from datetime import datetime, timezone


def test_parse():
    date_string = "2023-04-15 10:30:00"
    parsed_date = parse(date_string)
    assert isinstance(parsed_date, datetime)
    assert parsed_date.year == 2023
    assert parsed_date.month == 4
    assert parsed_date.day == 15
    assert parsed_date.hour == 10
    assert parsed_date.minute == 30


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
