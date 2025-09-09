def takes_positive(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            if arg <= 0:
                raise ValueError
            if not isinstance(arg, int):
                raise TypeError

            for kwarg in kwargs.values():
                if not isinstance(kwarg, int):
                    raise TypeError
                if kwarg <= 0:
                    raise ValueError

        return func(*args, **kwargs)
    return wrapper


@takes_positive
def positive_sum(*args):
    return sum(args)
try:
    print(positive_sum('10', 20, 10))
except Exception as err:
    print(type(err))