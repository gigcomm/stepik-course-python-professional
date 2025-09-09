import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            result_end = min(end, len(result))

            if start >=len(result):
                return result

            change = char * (result_end - start)

            return result[:start] + change + result[result_end:]
        return wrapper
    return decorator


@strip_range(3, 20, '_')
def beegeek():
    return 'beegeek'


print(beegeek())