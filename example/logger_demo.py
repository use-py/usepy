import threading
from fastapi import FastAPI
import uvicorn
from loguru import logger
from usepy import useLogger

def main():
    def uvicorn_run():
        # 拦截转发 uvicorn
        server = uvicorn.Server(uvicorn.Config(app=FastAPI(), host="0.0.0.0"))
        useLogger.intercept_uvicorn()  # 注意拦截时机，详看函数说明
        server.run()

    # 一键调用，logstash_handler 已过滤 uvicorn 的日志
    useLogger.init(logstash_extra={"app": "app"}, logger_extra={"app_name": "app_name"})


    # 分开调用，拦截并显示全部日志
    # useLogger.intercept()  # 拦截转发，留空=ALL
    # logger.add(**useLogger.default_handler(remove=True))
    # logger.add(**useLogger.logstash_handler(extra=dict(app_name="app_name")))
    # logger.configure(extra={"project_name": "project_name"})


    # 个性化配置
    # useLogger.intercept(("kit",))  # 拦截转发 指定的库
    # logger.configure(handlers=[
    #     useLogger.default_handler(level="DEBUG"),
    #     useLogger.logstash_handler(level="INFO", extra={"app_name": "app_name"},
    #                      filter=lambda record: "uvicorn" not in record["name"]),
    # ], extra={"project_name": "project_name"})


    # 测试输出日志
    logger.warning("test debug")
    logger.info("test info")
    logger.debug("test debug")
    logger.opt(raw=True).debug("No formatting\n")

    thread = threading.Thread(target=uvicorn_run).start()


if __name__ == '__main__':
    main()
