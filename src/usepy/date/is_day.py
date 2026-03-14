from datetime import datetime, date, timedelta
from typing import Union


def is_today(dt: Union[datetime, date, str]) -> bool:
    """
    Checks if a datetime/date is today.

    Args:
        dt (Union[datetime, date, str]): The datetime/date to check.

    Returns:
        bool: True if the date is today, False otherwise.

    Examples:
        >>> is_today(datetime.now())
        True
        >>> is_today(date.today())
        True
        >>> is_today('2023-01-01')
        False
    """
    if isinstance(dt, str):
        from usepy.date.parse import parse
        dt = parse(dt)
    
    if isinstance(dt, datetime):
        dt = dt.date()
    
    return dt == date.today()


def is_yesterday(dt: Union[datetime, date, str]) -> bool:
    """
    Checks if a datetime/date is yesterday.

    Args:
        dt (Union[datetime, date, str]): The datetime/date to check.

    Returns:
        bool: True if the date is yesterday, False otherwise.

    Examples:
        >>> is_yesterday(date.today() - timedelta(days=1))
        True
    """
    if isinstance(dt, str):
        from usepy.date.parse import parse
        dt = parse(dt)
    
    if isinstance(dt, datetime):
        dt = dt.date()
    
    return dt == date.today() - timedelta(days=1)


def is_tomorrow(dt: Union[datetime, date, str]) -> bool:
    """
    Checks if a datetime/date is tomorrow.

    Args:
        dt (Union[datetime, date, str]): The datetime/date to check.

    Returns:
        bool: True if the date is tomorrow, False otherwise.

    Examples:
        >>> is_tomorrow(date.today() + timedelta(days=1))
        True
    """
    if isinstance(dt, str):
        from usepy.date.parse import parse
        dt = parse(dt)
    
    if isinstance(dt, datetime):
        dt = dt.date()
    
    return dt == date.today() + timedelta(days=1)