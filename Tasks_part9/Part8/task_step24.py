import functools


def ignore_exception(*exception_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except exception_types as e:
                print(f"Исключение {type(e).__name__} обработано")
        return wrapper
    return decorator


min = ignore_exception(ZeroDivisionError)(min)
try:
    print(min(1, '2', 3, [4, 5]))
except Exception as e:
    print(type(e))
