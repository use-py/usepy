from datetime import datetime
from typing import Optional


def timestamp(dt: Optional[datetime] = None, digits: int = 10) -> int:
    """get timestamp from datetime object

    Args:
        dt (Optional[datetime], optional): datetime object. Defaults to None.
        digits (int, optional): timestamp digits, 10 or 13. Defaults to 10.

    Returns:
        int: integer timestamp
    """
    if dt is None:
        dt = datetime.now()

    if digits == 10:
        return int(dt.timestamp())
    elif digits == 13:
        return int(dt.timestamp() * 1000)
    else:
        raise ValueError("timestamp digits must be 10 or 13")


def to_datetime(ts: int) -> datetime:
    """convert timestamp to datetime

    Args:
        ts (int): timestamp, can be 10 or 13 digits

    Returns:
        datetime: datetime object
    """
    if len(str(ts)) == 13:
        return datetime.fromtimestamp(ts / 1000)
    elif len(str(ts)) == 10:
        return datetime.fromtimestamp(ts)
    else:
        raise ValueError("timestamp digits must be 10 or 13")
