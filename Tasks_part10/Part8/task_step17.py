from itertools import count, cycle


def alnum_sequence():
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    for i, letter in cycle(zip(count(1), alphabet)):
        yield i
        yield letter

alnum = alnum_sequence()
print(*(next(alnum) for _ in range(55)))
print()
alnum = alnum_sequence()
print(*(next(alnum) for _ in range(100)))