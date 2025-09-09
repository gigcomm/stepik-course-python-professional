import functools


def repeat(times):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator


@repeat(4)
def say_beegeek():
    '''documentation'''
    print('beegeek')

say_beegeek()
print(say_beegeek.__name__)
print(say_beegeek.__doc__)
