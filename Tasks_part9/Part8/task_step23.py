import functools


def add_attrs(**attrs):
    def decorator(func):
        func.__dict__.update(**attrs)
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator


@add_attrs(attr2='geek')
@add_attrs(attr1='bee')
def beegeek():
    return 'beegeek'

print(beegeek.attr1)
print(beegeek.attr2)
print(beegeek.__name__)
