import time

from ex2 import fetcher

CALL_COUNT = 10


def benchmark(num):
    def decorator(func):
        def wrapper(*args, **kwargs):
            sum = 0
            for i in range(num):
                start = time.time()
                func(*args, **kwargs)
                end = time.time()
                diff = end - start
                print(f'One call func time: {diff}')
                sum += diff
            print(f'Avg time: {sum / num}')
        return wrapper
    return decorator


@benchmark(CALL_COUNT)
def fetch_page(url):
    fetcher.get(url)
