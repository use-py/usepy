from datetime import datetime
from typing import Optional


def format(dt: datetime, fmt: Optional[str] = None) -> str:
    """format date

    Args:
        dt (datetime): The datetime to format.
        fmt (str, optional): The format of the datetime. Defaults to None.
    """
    _fmt = fmt or "%Y-%m-%d %H:%M:%S"
    return dt.strftime(_fmt)
