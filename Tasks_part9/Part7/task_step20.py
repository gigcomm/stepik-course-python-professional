def upper(func):
    def wrapper(*args, **kwargs):
        new_args = []
        for arg in args:
            if isinstance(arg, str):
                new_args.append(arg.upper())
            else:
                new_args.append(arg)

        if 'sep' in kwargs and isinstance(kwargs['sep'], str):
            kwargs['sep'] = kwargs['sep'].upper()
        if 'end' in kwargs and isinstance(kwargs['end'], str):
            kwargs['end'] = kwargs['end'].upper()

        return func(*new_args, **kwargs)
    return wrapper

print = upper(print)
print('hi', 'there', end='!')