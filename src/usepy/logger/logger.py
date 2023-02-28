"""
- logging 日志拦截转发到 loguru
- 日志输出为json并精简&自定义字段
- 日志拦截与输出的 集成&单独 方法
"""

try:
    from loguru import logger
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "You need install the 'loguru' module before use 'usepy.logger.*'"
    )
from typing import List, Tuple, Optional, Union

from .handlers import default_handler
from .intercept import intercept_logger


def init_logger(handlers: Optional[List[str]] = None, packages: Optional[Union[List[str], Tuple[str]]] = None, **kwargs):
    """
    为 kit.rpc 集成日志的处理，默认拦截kit和uvicorn的日志。
    所属程序本身的日志可直接 from loguru import logger

    # :param default: 默认 level=DEBUG ， 输出到 sys.stderr
    # :param logstash: 默认 level=INFO ， 输出为 json。过滤了 uvicorn 的日志
    # :param intercept: logging 要拦截的日志名列表，默认只拦截 kit，具体格式参考 intercept_logger()
    # :param logstash_extra: 要传递给 logstash_handler 的 JsonFormatter 的 kwargs 的参数
    # :param logger_extra: 要传递给 logger 的 extra 的参数
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

    logger.configure(handlers=handlers, extra=extra, **kwargs)
