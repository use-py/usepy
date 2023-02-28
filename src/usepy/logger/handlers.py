import logging
import sys

from .formatters import JsonFormatter

try:
    from loguru import logger
except ModuleNotFoundError as e:
    raise ModuleNotFoundError(
        "You need install the 'loguru' module before use 'usepy.utils.logger'"
    )

DEFAULT_HANDLER_FORMAT = "<green>{time:YYYY-mm-dd HH:mm:ss.SSS}</green> | " \
                         "<level>{level}</level> | <level>{message}</level>"
LOGSTASH_HANDLER_FORMAT = "{message}"


def default_handler(level="DEBUG", format=DEFAULT_HANDLER_FORMAT, **kwargs) -> dict:
    return dict(sink=sys.stderr, level=level, format=format, **kwargs)


class LogstashHandler(logging.StreamHandler):
    def __init__(self, formatter=None):
        super().__init__()
        self.formatter = formatter


def logstash_handler(
        level="INFO",
        format=LOGSTASH_HANDLER_FORMAT,
        filter=lambda record: "uvicorn" not in record["name"],
        extra=None,
        **kwargs
) -> dict:
    if extra is None:
        extra = {}
    elif not isinstance(extra, dict):
        raise TypeError(
            "The 'extra' parameter should be a dict (or None), not: '%s'"
            % type(extra).__name__
        )

    return dict(
        sink=LogstashHandler(JsonFormatter(**extra)),
        level=level,
        format=format,
        filter=filter,
        **kwargs
    )
