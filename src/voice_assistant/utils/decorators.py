import asyncio
import functools
import time

from voice_assistant.utils.log_utils import log_runtime


def timeit_decorator(func):
    @functools.wraps(func)
    async def async_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = await func(*args, **kwargs)
        duration = round(time.perf_counter() - start_time, 4)
        log_runtime(func.__name__, duration)
        return result

    @functools.wraps(func)
    def sync_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = round(time.perf_counter() - start_time, 4)
        log_runtime(func.__name__, duration)
        return result

    return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper
