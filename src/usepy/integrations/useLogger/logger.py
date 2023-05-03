"""
- logging 日志拦截转发到 loguru
- 日志输出为json并精简&自定义字段
- 日志拦截与输出的 集成&单独 方法
"""
from datetime import tzinfo
from typing import List, Tuple, Optional, Union, Dict

from loguru import logger

from .handlers import default_handler
from .intercept import intercept_logger


def init_logger(
        handlers: Optional[List[Dict]] = None,
        packages: Optional[Union[List[str], Tuple[str]]] = None,
        tz: Optional[tzinfo] = None,
        **kwargs
):
    """
    一键配置 loguru ，所属程序本身的日志可直接 from loguru import logger ，即可正常处理

    :param handlers: 日志处理的 handlers ，参见 loguru.configure ，默认配置了 default_handler ，其他预置的可以从 .logger.handlers 导入
    :param packages: 要拦截的日志名列表，默认不拦截，传空列表则全部拦截，具体格式参考 useLoggerIntercept()
    :param tz: 时区，datetime.tzinfo 类型，默认不转换时区
    :param kwargs: 其他要传递给 logger.configure 的参数
    """
    if handlers is None:
        handlers = [default_handler()]
    elif not isinstance(handlers, list):
        raise TypeError(
            "The 'handlers' parameter should be a list (or None), not: '%s'"
            % type(handlers).__name__
        )
    
    if packages is not None and not isinstance(packages, (tuple, list)):
        raise TypeError(
            "The 'packages' parameter should be a dict (or tuple or None), not: '%s'"
            % type(packages).__name__
        )
    
    extra = kwargs.pop("extra", {})
    if not isinstance(extra, dict):
        raise TypeError(
            "The 'extra' parameter should be a dict (or None), not: '%s'"
            % type(extra).__name__
        )
    
    if isinstance(packages, (tuple, list)):
        intercept_logger(packages, include_child=True)
    
    patcher = None if tz is None else lambda record: record.update(time=record["time"].astimezone(tz))
    logger.configure(handlers=handlers, extra=extra, patcher=patcher, **kwargs)
