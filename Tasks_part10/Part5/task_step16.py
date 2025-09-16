def alternating_sequence(count=None):
    n = 1
    if count is None:
        while True:
            if n % 2 == 0:
                yield -n
            else:
                yield n
            n += 1
    else:
        for i in range(1, count+1):
            if n % 2 == 0:
                yield -i
            else:
                yield i
            n += 1


generator = alternating_sequence(10)
print(*generator)
