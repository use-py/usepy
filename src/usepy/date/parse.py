from datetime import datetime
from itertools import chain


def parse(time_str: str, fmt=None) -> datetime:
    """parse date

    Args:
        time_str (str): The time string to parse.
        fmt (str, optional): The format of the time string. Defaults to None.

    Returns:
        datetime: The parsed datetime.
    """
    DATETIME_COMMON = (
        "%Y-%m-%d %H:%M:%S",
        "%Y-%m-%d %H:%M",
        "%Y/%m/%d %H:%M:%S",
        "%Y/%m/%d %H:%M",
        "%Y年%m月%d日%H:%M:%S",
        "%Y年%m月%d日 %H:%M:%S",
        "%Y年%m月%d日%H时%M分%S秒",
        "%Y年%m月%d日 %H时%M分%S秒",
    )
    DATE_FORMATS = (
        "%Y-%m-%d",
        "%Y%m%d",
        "%Y/%m/%d",
        "%Y.%m.%d",
        "%d.%m.%y",
        "%d.%m.%Y",
        "%Y %m %d",
        "%m/%d/%Y",
    )
    DATETIME_FORMATS = list(
        chain.from_iterable(
            [
                ["{} %H:%M:%S".format(fmt) for fmt in DATE_FORMATS],
                ["{} %H:%M".format(fmt) for fmt in DATE_FORMATS],
                ["{}T%H:%M:%S.%f%z".format(fmt) for fmt in DATE_FORMATS],
            ]
        )
    )
    s = time_str.strip()
    if fmt is not None:
        return datetime.strptime(s, fmt)
    for fmt in chain.from_iterable((DATETIME_COMMON, DATETIME_FORMATS, DATE_FORMATS)):
        try:
            return datetime.strptime(s, fmt)
        except ValueError:
            continue
    raise ValueError(f"No valid date format found for '{s}'")
