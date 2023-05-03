import logging
from types import FrameType
from typing import Tuple, cast, Optional, List, Union

from loguru import logger


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
            level,
            record.getMessage(),
        )


def intercept_logger(names: Optional[Union[List[str], Tuple[str]]] = None, include_child=False):
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
            intercept_logger()
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


UVICORN_LOGGER_NAMES = ["uvicorn", "uvicorn.asgi", "uvicorn.access"]


def intercept_uvicorn_logger():
    """
    使用 loguru 拦截 uvicorn 日志

    注意拦截时机，在 app 实例化之前调用即可，例子：
    --------
    >>> from fastapi import FastAPI
    >>> from usepy.logger import useLoggerInterceptUvicorn
    >>>
    >>> useLoggerInterceptUvicorn()  # 在 app 实例化前调用即可
    >>> app = FastAPI()
    >>>
    >>> ...
    """
    intercept_logger(UVICORN_LOGGER_NAMES, include_child=True)
