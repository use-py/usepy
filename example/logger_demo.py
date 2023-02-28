from fastapi import FastAPI
from loguru import logger

from usepy.logger import (
    useLogger,
    useLoggerIntercept,
    useLoggerInterceptUvicorn,
    default_handler,
    logstash_handler
)
from usepy.logger import useLoggerInterceptUvicorn

useLoggerInterceptUvicorn()  # 在 app 实例化前调用即可

app = FastAPI()


@app.get("/")
def home():
    return {"message": "hello"}


if __name__ == '__main__':
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
    # useLoggerIntercept(("kit",))  # 拦截转发 指定的库
    # logger.configure(
    #     handlers=[
    #         default_handler(level="TRACE"),
    #         logstash_handler(level="WARNING", extra={"app_name": "app_name"}),
    #     ],
    #     extra={"project_name": "project_name"}
    # )

    # 测试输出日志
    logger.warning("test debug")
    logger.info("test info")
    logger.debug("test debug")
    logger.opt(raw=True).debug("No formatting\n")

    import uvicorn
    uvicorn.run(app="app:app", host="127.0.0.1", reload=False, workers=2)
