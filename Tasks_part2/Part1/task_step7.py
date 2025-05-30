def print_given(*args, **kwargs):
    for arg in args:
        print(f"{arg} {type(arg)}")
    for key, value in sorted(kwargs.items()):
        print(f"{key} {value} {type(value)}")

print_given(1, [1, 2, 3], 'three', two=2)