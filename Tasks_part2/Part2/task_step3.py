n, X, Y, A, B = map(int, input().split())

numbers = list(range(1, n + 1))

numbers[X - 1:Y] = reversed(numbers[X - 1:Y])
numbers[A - 1:B] = reversed(numbers[A - 1:B])

print(*numbers)
