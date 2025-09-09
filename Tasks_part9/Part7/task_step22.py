def reverse_args(func):
    def wrapper(*args, **kwargs):
        reverse_args = reversed(args)
        return func(*reverse_args, **kwargs)

    return wrapper

@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))