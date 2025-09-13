def starmap(func, iterable):
    return map(lambda args: func(*args), iterable)

points = [(1, 1, 1), (1, 1, 2), (2, 2, 3)]
print(*starmap(lambda x, y, z: x * y * z, points))