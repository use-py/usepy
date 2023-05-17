try:
    from typing import Literal
except ImportError:
    from typing_extensions import Literal
import calendar
from datetime import datetime, timedelta
from itertools import chain
from typing import Optional

UnitType = Optional[
    Literal[
        "year", "month", "day", "today", "hour", "minute",
    ]
]

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


class useDateTime:
    DAYS = 'days'
    HOURS = 'hours'
    MINUTES = 'minutes'
    SECONDS = 'seconds'
    MILLISECONDS = 'milliseconds'
    MICROSECONDS = 'microseconds'

    @staticmethod
    def now() -> datetime:
        """
        获取当前时间
        :return: 当前时间
        """
        return datetime.now()

    format_now = staticmethod(lambda fmt=None: useDateTime.format(useDateTime.now(), fmt))

    @staticmethod
    def last(dt: datetime, unit: UnitType) -> datetime:
        """
        获取最后一天/一年/一月/一小时/一分钟/一秒
        :param dt: 时间
        :param unit:
        :return: 时间
        """
        last_dt = dt.replace(hour=23, minute=59, second=59, microsecond=999999)
        unit_map = {
            'year': lambda x: x.replace(month=12, day=31),
            'month': lambda x: x.replace(day=calendar.monthrange(x.year, x.month)[1]),
            'day': lambda x: x,
            'today': lambda x: x,
            'hour': lambda x: x.replace(hour=dt.hour),
            'minute': lambda x: x.replace(hour=dt.hour, minute=dt.minute)
        }
        return unit_map.get(unit, lambda x: x)(last_dt)

    @staticmethod
    def first(dt: datetime, unit: UnitType) -> datetime:
        """
        获取第一天/一年/一月/一小时/一分钟/一秒
        :param dt: 时间
        :param unit:
        :return: 时间
        """
        first_dt = dt.replace(hour=0, minute=0, second=0, microsecond=0)
        unit_map = {
            'year': lambda x: x.replace(month=1, day=1),
            'month': lambda x: x.replace(day=1),
            'day': lambda x: x,
            'today': lambda x: x,
            'hour': lambda x: x.replace(hour=dt.hour),
            'minute': lambda x: x.replace(hour=dt.hour, minute=dt.minute)
        }
        return unit_map.get(unit, lambda x: x)(first_dt)

    @staticmethod
    def timestamp(dt: Optional[datetime] = None, digit: int = 10) -> int:
        """
        获取当前时间戳，默认10位
        :param dt: 时间，默认当前时间
        :param digit: 位数
        :return: 时间戳
        >>> useDateTime.timestamp()
        1600000000
        >>> useDateTime.timestamp(digit=13)
        1600000000000
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
    def before(nums, unit=None) -> datetime:
        """
        获取指定单位的时间
        :param nums: 数量
        :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
        :return: 时间
        """
        _unit = unit or 'days'
        return datetime.now() - timedelta(**{_unit: nums})

    format_before = staticmethod(
        lambda nums, unit=None, fmt=None: useDateTime.format(useDateTime.before(nums, unit), fmt)
    )

    @staticmethod
    def after(nums, unit=None) -> datetime:
        """
        获取指定单位的时间
        :param nums: 数量
        :param unit: 单位，支持：days[默认], seconds, microseconds, milliseconds, minutes, hours, weeks
        :return: 时间
        """
        _unit = unit or 'days'
        return datetime.now() + timedelta(**{_unit: nums})

    format_after = staticmethod(
        lambda nums, unit=None, fmt=None: useDateTime.format(useDateTime.after(nums, unit), fmt)
    )

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

    @staticmethod
    def humanize(dt: datetime, rel_dt: datetime = None) -> str:
        """
        人性化时间
        :param dt: 时间
        :param rel_dt: 相对时间 默认当前时间
        :return: 人性化时间
        """
        rel_dt = rel_dt or datetime.now()
        diff_dt = rel_dt - dt

        diff_seconds = diff_dt.total_seconds()
        if 0 <= diff_seconds <= 60:
            return '刚刚'

        chunks = (
            (60 * 60 * 24 * 365, '年'),
            (60 * 60 * 24 * 30, '月'),
            (60 * 60 * 24 * 7, '周'),
            (60 * 60 * 24, '天'),
            (60 * 60, '小时'),
            (60, '分钟'),
        )
        er_val = 10  # 误差值
        tense = '前' if diff_seconds > 0 else '后'
        diff_seconds = abs(diff_seconds)

        for seconds, unit in chunks:
            count = (diff_seconds + er_val) // seconds
            if count != 0:
                return str(int(count)) + unit + tense
        return '未知'
