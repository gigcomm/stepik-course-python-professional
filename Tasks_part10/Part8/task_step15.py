from itertools import count, starmap


def tabulate(func):
     n = 1
     while True:
         yield func(n)
         n += 1

func = lambda x: x
values = tabulate(func)
print(next(values))
print(next(values))

func = lambda x: x + 10
values = tabulate(func)
print(next(values))
print(next(values))
print(next(values))