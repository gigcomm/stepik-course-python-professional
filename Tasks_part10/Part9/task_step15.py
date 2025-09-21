from itertools import compress, islice


def take(iterable, n):
    return islice(iterable, n)


iterator = iter('beegeek')
print(*take(iterator, 22))

iterator = iter('beegeek')
print(*take(iterator, 1))
