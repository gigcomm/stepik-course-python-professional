import random


def random_numbers(left, right):
    return iter(lambda: random.randint(left, right), None)


iterator = random_numbers(1, 10)
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
print(next(iterator) in range(1, 11))
