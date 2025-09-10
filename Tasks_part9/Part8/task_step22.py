import functools


def takes(*expected_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            for arg in args:
                if not any(isinstance(arg, type) for type in expected_types):
                    raise TypeError

            return result
        return wrapper
    return decorator

@takes(int, str)
def repeat_string(string, times):
    return string * times
print(repeat_string('bee', 3))