import time
from functools import wraps


def timeit(ret_time=False):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            st = time.perf_counter()
            r = func(*args, **kwargs)
            et = time.perf_counter()
            print('{}: {:.16f} ns'.format(func.__name__, et - st))
            return (et - st, r,) if ret_time else r

        return wrapped

    return decorator
