def palindromes():
    yield from range(1, 10)

    n = 11
    while True:
        s = str(n)
        if s == s[::-1]:
            yield n
        n += 1



generator = palindromes()
numbers = [next(generator) for _ in range(30)]
print(*numbers)
