import pytest
from datetime import datetime, date, timedelta
from usepy.date import is_today, is_yesterday, is_tomorrow, add_days, add_months, diff_days


class TestIsToday:
    """Tests for is_today() function"""

    def test_is_today_datetime(self):
        """Test is_today with datetime"""
        assert is_today(datetime.now()) is True

    def test_is_today_date(self):
        """Test is_today with date"""
        assert is_today(date.today()) is True

    def test_is_today_yesterday(self):
        """Test is_today with yesterday"""
        assert is_today(date.today() - timedelta(days=1)) is False

    def test_is_today_tomorrow(self):
        """Test is_today with tomorrow"""
        assert is_today(date.today() + timedelta(days=1)) is False

    def test_is_today_string(self):
        """Test is_today with string"""
        today_str = date.today().strftime('%Y-%m-%d')
        assert is_today(today_str) is True
        assert is_today('2023-01-01') is False


class TestIsYesterday:
    """Tests for is_yesterday() function"""

    def test_is_yesterday_true(self):
        """Test is_yesterday with yesterday"""
        assert is_yesterday(date.today() - timedelta(days=1)) is True

    def test_is_yesterday_today(self):
        """Test is_yesterday with today"""
        assert is_yesterday(date.today()) is False

    def test_is_yesterday_datetime(self):
        """Test is_yesterday with datetime"""
        yesterday = datetime.now() - timedelta(days=1)
        assert is_yesterday(yesterday) is True


class TestIsTomorrow:
    """Tests for is_tomorrow() function"""

    def test_is_tomorrow_true(self):
        """Test is_tomorrow with tomorrow"""
        assert is_tomorrow(date.today() + timedelta(days=1)) is True

    def test_is_tomorrow_today(self):
        """Test is_tomorrow with today"""
        assert is_tomorrow(date.today()) is False

    def test_is_tomorrow_datetime(self):
        """Test is_tomorrow with datetime"""
        tomorrow = datetime.now() + timedelta(days=1)
        assert is_tomorrow(tomorrow) is True


class TestAddDays:
    """Tests for add_days() function"""

    def test_add_days_positive(self):
        """Test adding positive days"""
        result = add_days(date(2023, 1, 1), 5)
        assert result == date(2023, 1, 6)

    def test_add_days_negative(self):
        """Test subtracting days"""
        result = add_days(date(2023, 1, 10), -5)
        assert result == date(2023, 1, 5)

    def test_add_days_zero(self):
        """Test adding zero days"""
        result = add_days(date(2023, 1, 1), 0)
        assert result == date(2023, 1, 1)

    def test_add_days_datetime(self):
        """Test adding days to datetime"""
        result = add_days(datetime(2023, 1, 1, 12, 30), 3)
        assert result == datetime(2023, 1, 4, 12, 30)

    def test_add_days_string(self):
        """Test adding days to string date"""
        result = add_days('2023-01-01', 5)
        assert result == datetime(2023, 1, 6)


class TestAddMonths:
    """Tests for add_months() function"""

    def test_add_months_positive(self):
        """Test adding positive months"""
        result = add_months(date(2023, 1, 15), 2)
        assert result == date(2023, 3, 15)

    def test_add_months_negative(self):
        """Test subtracting months"""
        result = add_months(date(2023, 3, 15), -2)
        assert result == date(2023, 1, 15)

    def test_add_months_year_rollover(self):
        """Test month addition with year rollover"""
        result = add_months(date(2023, 11, 15), 3)
        assert result == date(2024, 2, 15)

    def test_add_months_day_overflow(self):
        """Test month addition with day overflow"""
        # Jan 31 -> Feb 28 (non-leap year)
        result = add_months(date(2023, 1, 31), 1)
        assert result == date(2023, 2, 28)

    def test_add_months_leap_year(self):
        """Test month addition in leap year"""
        # Jan 31 -> Feb 29 (leap year)
        result = add_months(date(2024, 1, 31), 1)
        assert result == date(2024, 2, 29)


class TestDiffDays:
    """Tests for diff_days() function"""

    def test_diff_days_positive(self):
        """Test positive difference"""
        result = diff_days(date(2023, 1, 10), date(2023, 1, 5))
        assert result == 5

    def test_diff_days_negative(self):
        """Test negative difference"""
        result = diff_days(date(2023, 1, 5), date(2023, 1, 10))
        assert result == -5

    def test_diff_days_zero(self):
        """Test zero difference"""
        result = diff_days(date(2023, 1, 1), date(2023, 1, 1))
        assert result == 0

    def test_diff_days_datetime(self):
        """Test difference with datetime"""
        result = diff_days(datetime(2023, 1, 10, 12, 0), datetime(2023, 1, 5, 8, 0))
        assert result == 5

    def test_diff_days_string(self):
        """Test difference with string dates"""
        result = diff_days('2023-01-10', '2023-01-05')
        assert result == 5