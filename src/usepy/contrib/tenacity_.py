import typing as t
from inspect import iscoroutinefunction

from tenacity import (
    retry as _retry,
    stop_after_attempt, stop_never, wait_fixed,
    retry_if_result, retry_if_exception_type
)

undefined = object()


def retry(max_times: t.Optional[int] = None,
          wait_times: t.Optional[int] = None,
          retry_on_result=undefined,
          retry_on_exception: t.Union[
              t.Type[BaseException],
              t.Tuple[t.Type[BaseException], ...],
          ] = Exception,
          *t_args, **t_kw):
    """
    包装tenacity.retry，让调用更简易些
    :param max_times: 最大重试次数
    :param wait_times: 每次重试等待时间
    :param retry_on_result: 当返回值等于retry_on_result时，重试
    :param retry_on_exception: 当抛出指定异常时，重试
    :param t_args: tenacity.retry的参数
    :param t_kw: tenacity.retry的参数
    :return:
    """

    stop_on = stop_never if max_times is None else stop_after_attempt(max_times)

    retry_on = retry_if_exception_type(retry_on_exception)
    if retry_on_result is not undefined:
        retry_on = retry_if_result(lambda result: result == retry_on_result) | retry_on

    wait_on = wait_fixed(wait_times) if wait_times is not None else wait_fixed(0)

    def decorator(func):

        if iscoroutinefunction(func):
            @_retry(retry=retry_on, stop=stop_on, wait=wait_on, *t_args, **t_kw)
            async def wrapper(*args, **kwargs):
                return await func(*args, **kwargs)

            return wrapper

        else:
            @_retry(retry=retry_on, stop=stop_on, wait=wait_on, *t_args, **t_kw)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)

            return wrapper

    return decorator


if __name__ == '__main__':
    @retry(max_times=3, wait_times=1, retry_on_result=None, retry_error_callback=lambda x: print("123"))
    async def maybe_none():
        print("111111")
        return None


    import asyncio

    asyncio.run(maybe_none())
