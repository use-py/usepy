from datetime import datetime


def format(dt: datetime, fmt=None) -> str:
    """format date

    Args:
        dt (datetime): The datetime to format.
        fmt (str, optional): The format of the datetime. Defaults to None.
    """
    _fmt = fmt or "%Y-%m-%d %H:%M:%S"
    return dt.strftime(_fmt)
