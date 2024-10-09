from datetime import datetime
from typing import Optional


def timestamp(dt: Optional[datetime] = None, digits: Optional[int] = 10) -> int:
    """
    get timestamp from datetime object

    :param dt: datetime object, default to current time
    :param digits: timestamp digits, 10 or 13, default to 10
    :return: integer timestamp
    """
    if dt is None:
        dt = datetime.now()

    if digits == 10:
        return int(dt.timestamp())
    elif digits == 13:
        return int(dt.timestamp() * 1000)
    else:
        raise ValueError("timestamp digits must be 10 or 13")
