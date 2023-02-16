from datetime import datetime, timedelta
from itertools import chain
from typing import Optional

DATETIME_COMMON = (
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%d %H:%M",
    "%Y/%m/%d %H:%M:%S",
    "%Y/%m/%d %H:%M",
    "%Y年%m月%d日%H:%M:%S",
    "%Y年%m月%d日 %H:%M:%S",
    "%Y年%m月%d日%H时%M分%S秒",
    "%Y年%m月%d日 %H时%M分%S秒"
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
            ["{}T%H:%M:%S.%f%z".format(fmt) for fmt in DATE_FORMATS]
        ]
    )
)


class UseDateTime:
    DAYS = 'days'
    HOURS = 'hours'
    MINUTES = 'minutes'
    SECONDS = 'seconds'
    MILLISECONDS = 'milliseconds'
    MICROSECONDS = 'microseconds'

    @staticmethod
    def timestamp(dt: Optional[datetime] = None, digit: int = 10) -> int:
        """
        获取当前时间戳，默认10位
        :param dt: 时间，默认当前时间
        :param digit: 位数
        :return: 时间戳
        """
        if not dt:
            dt = datetime.now()
        if digit == 10:
            return int(dt.timestamp())
        elif digit == 13:
            return int(dt.timestamp() * 1000)
        else:
            raise ValueError('digit must be 10 or 13')

    @staticmethod
    def format(dt: datetime, fmt=None) -> str:
        """
        格式化时间
        :param dt:
        :param fmt: 时间格式
        :return: 时间
        """
        _fmt = fmt or '%Y-%m-%d %H:%M:%S'
        return dt.strftime(_fmt)

    @staticmethod
    def format_now(fmt=None) -> str:
        """
        获取当前时间
        :param fmt: 时间格式
        :return: 时间
        """
        return UseDateTime.format(datetime.now(), fmt)

    @staticmethod
    def format_before(nums, unit=None, fmt=None) -> str:
        """
        获取指定单位的时间
        :param nums: 数量
        :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
        :param fmt: 时间格式
        :return: 时间
        """
        _unit = unit or 'days'
        return UseDateTime.format(datetime.now() - timedelta(**{_unit: nums}), fmt)

    @staticmethod
    def format_after(nums, unit=None, fmt=None) -> str:
        """
        获取指定单位的时间
        :param nums: 数量
        :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
        :param fmt: 时间格式
        :return: 时间
        """
        _unit = unit or 'days'
        return UseDateTime.format(datetime.now() + timedelta(**{_unit: nums}), fmt)

    @staticmethod
    def parse(time_str: str, fmt=None) -> datetime:
        """
        解析时间
        :param time_str: 时间字符串
        :param fmt: 时间格式
        :return: 时间
        """
        s = time_str.strip()
        if fmt is not None:
            return datetime.strptime(s, fmt)
        for fmt in chain.from_iterable((DATETIME_COMMON,
                                        DATETIME_FORMATS,
                                        DATE_FORMATS)):
            try:
                return datetime.strptime(s, fmt)
            except ValueError:
                continue
        raise ValueError(f"No valid date format found for '{s}'")


useDateTime = UseDateTime
