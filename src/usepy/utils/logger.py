"""
- logging 日志拦截转发到 loguru
- 日志输出为json并精简&自定义字段
- 日志拦截与输出的 集成&单独 方法
"""

try:
    from loguru import logger
except ModuleNotFoundError as e:
    raise ModuleNotFoundError("You need install the 'loguru' module before use 'usepy.utils.logger'")

import json
import logging
import sys
from types import FrameType
from typing import cast, Dict, Tuple

JSONFORMATTER_EXTRA_IGNORE_FIELDS_DEFAULT = {
    'name', 'msg', 'args', "levelname", 'levelno', 'pathname', 'filename', 'module', 'exc_info', 'exc_text',
    'stack_info', 'lineno', 'funcName', 'created', 'msecs', 'relativeCreated', 'thread', 'threadName', 'processName',
    'process'
}


class JsonFormatter(logging.Formatter):
    """格式化日志到Json，并删除某些字段"""

    def __init__(self, extra_keep_fields: Tuple = ('levelname',), **kwargs):
        """
        :param extra_keep_fields: 会忽略 record[extra] 里大多数的默认字段，需要额外保留的字段就写在这里
        :param kwargs: 这里的 key:val 会添加到格式化后的消息中 eg: app=explore
        """
        super(JsonFormatter, self).__init__()
        self.extra_ignore_keys = JSONFORMATTER_EXTRA_IGNORE_FIELDS_DEFAULT - set(extra_keep_fields)
        self.kwargs = kwargs

    def formatException(self, exc_info):
        exc_text = super(JsonFormatter, self).formatException(exc_info)
        return repr(exc_text)

    def format(self, record):
        message = {
            **self.kwargs,
            "timestamp": self.format_timestamp(record.created),
            **self.get_extra_info(record)
        }

        if record.exc_info:
            message['message'] = self.formatException(record.exc_info)
            message['stack_trace'] = ''.join(record.getMessage().split('\n'))
        else:
            message['message'] = record.getMessage()

        return json.dumps(message)

    @classmethod
    def format_timestamp(cls, time):
        return int(time * 1000)

    def get_extra_info(self, record):
        return {
            attr_name: record.__dict__[attr_name]
            for attr_name in record.__dict__
            if attr_name not in self.extra_ignore_keys
        }


class LogstashHandler(logging.StreamHandler):
    def __init__(self, formatter=None):
        super().__init__()
        self.formatter = formatter


class InterceptHandler(logging.Handler):
    """拦截 logging 的消息并转发给 loguru"""

    def emit(self, record: logging.LogRecord) -> None:  # pragma: no cover
        # Get corresponding Loguru level if it exists
        try:
            level = logger.level(record.levelname).name
        except ValueError:
            level = str(record.levelno)

        # Find caller from where originated the logged message
        frame, depth = logging.currentframe(), 2
        while frame.f_code.co_filename == logging.__file__:  # noqa: WPS609
            frame = cast(FrameType, frame.f_back)
            depth += 1

        logger.opt(depth=depth, exception=record.exc_info).log(
            level, record.getMessage(),
        )


UVICORN_LOGGER_NAMES = ("uvicorn", "uvicorn.asgi", "uvicorn.access")
DEFAULT_FORMAT = "<green>{time:YYYY-mm-dd HH:mm:ss.SSS}</green> | <level>{level}</level> | <level>{message}</level>"

class Logger:

    @staticmethod
    def intercept(names: Tuple = None, include_child=False):
        """
        使用 loguru 拦截 指定的 logging 日志

        :param names: 要拦截的日志名列表，留空=拦截所有已设置的日志名，
                    None 或 ("",)：表示全部拦截
                    ("lib", "lib.sub", )：表示具体要拦截的日志名列表
                    ("", "lib", "lib.sub", )：表示先执行全部拦截，再按剩余名称拦截
        :param include_child: 包含对子模块的拦截，默认=False

        """

        if names is None:
            names = [name for name in logging.root.manager.loggerDict]
            # logger.debug(logger_names)
        else:
            first, *names = names
            if first in ["", None]:
                Logger.intercept()
            else:
                names.insert(0, first)

        for name in names:
            logging_logger = logging.getLogger(name)
            if logging_logger.level == 0:  # logging 中 level 0 在 loguru 记录不到
                logging_logger.setLevel(5)  # 所以修改为 level=TRACE
            # 替换 handlers 为 loguru 的拦截类（排除子模块时为空）
            if '.' in name and not include_child:
                logging_logger.handlers = []
            else:
                logging_logger.handlers = [InterceptHandler()]
                # logger.debug(f"{name} hooked. level={logging_logger.level}")

    @staticmethod
    def intercept_uvicorn():
        """
        使用 loguru 拦截 uvicorn 日志

        需要注意拦截时机，在Config后，run之前拦截，才能全部拦截，例子：
        --------
        >>> server = uvicorn.Server(uvicorn.Config(
        ...    app='web:app',
        ...    host=settings.server.host,
        ...    port=settings.server.port,
        ...    reload=settings.server.reload
        ... ))
        >>> intercept_uvicorn_logger()
        >>> server.run()
        """
        Logger.intercept(UVICORN_LOGGER_NAMES, include_child=True)

    @staticmethod
    def init(*, default=True, logstash=True, intercept=None,
                logstash_extra=None, logger_extra=None, **kwargs):
        """
        集成日志的处理，默认拦截uvicorn的日志。
        所属程序本身的日志可直接 from loguru import logger

        :param default: 默认 level=DEBUG ， 输出到 sys.stderr
        :param logstash: 默认 level=INFO ， 输出为 json。默认已过滤了 uvicorn 的日志
        :param intercept: logging 要拦截的日志名列表，默认已拦截 uvicorn，具体格式参考 intercept_logger()
        :param logstash_extra: 要传递给 logstash_handler 的 JsonFormatter 的 kwargs 的参数
        :param logger_extra: 要传递给 loguru.logger.configure 的 extra 的参数
        """
        if isinstance(intercept, (tuple, list)):
            Logger.intercept(intercept, include_child=True)

        handlers = []
        if default is True:
            handlers.append(Logger.default_handler())
        elif isinstance(default, dict):
            handlers.append(default)

        if logstash is True:
            logstash_extra = logstash_extra if isinstance(logstash_extra, dict) else {}
            handlers.append(Logger.logstash_handler(extra=logstash_extra, filter=lambda record: "uvicorn" not in record["name"]))
        elif isinstance(logstash, dict):
            handlers.append(logstash)

        logger_extra = logger_extra if isinstance(logger_extra, dict) else {}
        logger.configure(handlers=handlers, extra=logger_extra, **kwargs)

    @staticmethod
    def default_handler(level: str = "DEBUG", fmt: str = DEFAULT_FORMAT, remove=False, **kwargs):
        if remove:
            logger.remove()
        return dict(sink=sys.stderr, level=level, format=fmt, **kwargs)

    @staticmethod
    def logstash_handler(level: str = "INFO", fmt: str = "{message}", extra: Dict = None, remove=False, **kwargs):
        if remove:
            logger.remove()
        if extra is None:
            extra = {}
        return dict(sink=LogstashHandler(JsonFormatter(**extra)), level=level, format=fmt, **kwargs)