from itertools import product


def password_gen():
    return (''.join(map(str, item)) for item in product(range(10), repeat=3))

passwords = password_gen()
print(next(passwords))
print(next(passwords))
print(next(passwords))