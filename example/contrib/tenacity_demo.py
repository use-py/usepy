import asyncio

from usepy.contrib.tenacity_ import retry

if __name__ == "__main__":

    @retry(
        max_times=3,
        wait_times=1,
        retry_on_result=None,
        retry_error_callback=lambda x: print("123"),
    )
    def demo():
        print("test")
        return None

    @retry(
        max_times=3,
        wait_times=1,
        retry_on_result=None,
        retry_error_callback=lambda x: print("123"),
    )
    async def async_demo():
        print("async_demo")
        return None

    demo()
    asyncio.run(async_demo())
