import threading
from typing import Any
from fastapi import FastAPI
import uvicorn
from loguru import logger
from usepy.logger import (
    useLogger,
    useLoggerIntercept,
    useLoggerInterceptUvicorn,
    default_handler,
    logstash_handler
)


def main():
    def uvicorn_run():
        # 拦截转发 uvicorn
        server = uvicorn.Server(uvicorn.Config(app=FastAPI(), host="0.0.0.0"))
        useLoggerInterceptUvicorn()  # 注意拦截时机，详看函数说明
        server.run()

    # 一键调用，默认为 default_handler
    # useLogger()
    # useLogger(extra={"project_name": "project_name"})

    # 一键调用，配置多个 handler 和 packages
    useLogger(
        handlers=[
            default_handler(),
            logstash_handler(extra={"app_name": "app_name"})
        ],
        packages=["kit", "mylib.sublib"],
        extra={"project_name": "project_name"}
    )

    # 分开调用，拦截并显示全部日志
    # useLoggerIntercept()  # 拦截转发，留空=ALL
    # logger.remove()
    # logger.add(**default_handler())
    # logger.add(**logstash_handler(extra=dict(app_name="app_name")))
    # logger.configure(extra={"project_name": "project_name"})

    # 个性化配置
    useLoggerIntercept(("kit",))  # 拦截转发 指定的库
    logger.configure(
        handlers=[
            default_handler(level="TRACE"),
            logstash_handler(level="WARNING", extra={"app_name": "app_name"}),
        ],
        extra={"project_name": "project_name"}
    )

    # 测试输出日志
    logger.warning("test debug")
    logger.info("test info")
    logger.debug("test debug")
    logger.opt(raw=True).debug("No formatting\n")

    threading.Thread(target=uvicorn_run).start()


if __name__ == '__main__':
    main()

    """
    from usepy.logger import useLogger, defaultHandler, logstashHandler

    useLogger(
        handlers=[
            defaultHandler(level="DEBUG", ),
            logstashHandler(
                level="INFO",
                format=JsonFormatter(),
                filter=lambda record: "uvicorn" not in record["name"],
                extra={"app_name": "app_name"}
            )
        ],
        packages=["kit"],
        extra={"project_name": "project_name"}
    )

    useLogger(
        handlers=[
            defaultHandler(),
        ],
    )

    """
