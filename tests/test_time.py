from datetime import datetime, timedelta, timezone

from usepy import useDateTime


def test_parse():
    assert useDateTime.parse('2020-01-01 00:00:00') == datetime(2020, 1, 1, 0, 0)


def test_format():
    assert useDateTime.format(datetime(2022, 2, 1, 0, 0)) == '2022-02-01 00:00:00'
    assert useDateTime.format(datetime(2022, 2, 1, 0, 0), fmt='%Y-%m-%d') == '2022-02-01'
    assert useDateTime.format_before(1, useDateTime.DAYS) == useDateTime.format(datetime.now() - timedelta(days=1))
    assert useDateTime.format_after(3, useDateTime.HOURS) == useDateTime.format(datetime.now() + timedelta(hours=3))


def test_timestamp():
    assert useDateTime.timestamp(datetime(2022, 2, 1, 0, 0, 0, tzinfo=timezone.utc)) == 1643673600


def test_format_now():
    assert useDateTime.format_now() == useDateTime.format(datetime.now())
    assert useDateTime.format_now(fmt="%Y-%m-%d") == useDateTime.format(datetime.now(), "%Y-%m-%d")
