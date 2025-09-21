from itertools import takewhile


def first_true(iterable, predicate):
    if predicate is None:
        predicate = bool

    for item in iterable:
        if predicate(item):
            return item
    return None


numbers = [1, 1, 1, 1, 2, 4, 5, 6]
print(first_true(numbers, lambda num: num % 2 == 0))
