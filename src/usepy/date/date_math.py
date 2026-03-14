from datetime import datetime, date, timedelta
from typing import Union


def add_days(dt: Union[datetime, date, str], days: int) -> Union[datetime, date]:
    """
    Adds (or subtracts) days from a datetime/date.

    Args:
        dt (Union[datetime, date, str]): The datetime/date to modify.
        days (int): The number of days to add (negative to subtract).

    Returns:
        Union[datetime, date]: The new datetime/date with days added.

    Examples:
        >>> add_days(date(2023, 1, 1), 5)
        datetime.date(2023, 1, 6)
        >>> add_days(datetime(2023, 1, 1, 12, 0), -3)
        datetime.datetime(2022, 12, 29, 12, 0)
    """
    if isinstance(dt, str):
        from usepy.date.parse import parse
        dt = parse(dt)
    
    return dt + timedelta(days=days)


def add_months(dt: Union[datetime, date, str], months: int) -> Union[datetime, date]:
    """
    Adds (or subtracts) months from a datetime/date.

    Args:
        dt (Union[datetime, date, str]): The datetime/date to modify.
        months (int): The number of months to add (negative to subtract).

    Returns:
        Union[datetime, date]: The new datetime/date with months added.

    Examples:
        >>> add_months(date(2023, 1, 15), 2)
        datetime.date(2023, 3, 15)
        >>> add_months(date(2023, 3, 31), -1)
        datetime.date(2023, 2, 28)
    """
    if isinstance(dt, str):
        from usepy.date.parse import parse
        dt = parse(dt)
    
    # Calculate new month and year
    year = dt.year
    month = dt.month + months
    
    # Handle month overflow/underflow
    while month > 12:
        month -= 12
        year += 1
    while month < 1:
        month += 12
        year -= 1
    
    # Handle day overflow (e.g., Jan 31 -> Feb 28/29)
    day = min(dt.day, [31, 29 if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) else 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][month - 1])
    
    if isinstance(dt, datetime):
        return datetime(year, month, day, dt.hour, dt.minute, dt.second, dt.microsecond)
    else:
        return date(year, month, day)


def diff_days(dt1: Union[datetime, date, str], dt2: Union[datetime, date, str]) -> int:
    """
    Calculates the difference in days between two dates.

    Args:
        dt1 (Union[datetime, date, str]): The first datetime/date.
        dt2 (Union[datetime, date, str]): The second datetime/date.

    Returns:
        int: The difference in days (dt1 - dt2).

    Examples:
        >>> diff_days('2023-01-10', '2023-01-05')
        5
        >>> diff_days(date(2023, 1, 1), date(2023, 1, 5))
        -4
    """
    if isinstance(dt1, str):
        from usepy.date.parse import parse
        dt1 = parse(dt1)
    if isinstance(dt2, str):
        from usepy.date.parse import parse
        dt2 = parse(dt2)
    
    if isinstance(dt1, datetime):
        dt1 = dt1.date()
    if isinstance(dt2, datetime):
        dt2 = dt2.date()
    
    return (dt1 - dt2).days