from loguru import logger

from usepy.plugin import useLogger

useLogger(packages=["scrapy", "django", "usepy"])
logger.info("Hello World")
