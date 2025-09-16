def simple_sequence():
    count = 1
    while True:
        for _ in range(count):
            yield count
        count += 1


generator = simple_sequence()
numbers = [next(generator) for _ in range(10)]
print(*numbers)