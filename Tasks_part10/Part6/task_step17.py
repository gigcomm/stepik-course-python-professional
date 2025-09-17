def count_iterable(iterable):
    return len(list(iterable))


numbers = iter([1, 2, 3, 4, 5, 6, 7])
print(count_iterable(numbers))


data = tuple(range(432, 3845, 17))
print(count_iterable(data))