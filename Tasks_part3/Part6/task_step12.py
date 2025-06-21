import time
from math import factorial

def factorial_recurrent(n):
    if n == 0:
        return 1
    return n * factorial_recurrent(n - 1)

def factorial_classic(n):
    f = 1
    for i in range(2, n + 1):
        f *= i
    return f

def calculate_time(func, value):
    start_time = time.perf_counter()
    func(value)
    end_time = time.perf_counter()
    return end_time - start_time

print(calculate_time(factorial, 900))
print(calculate_time(factorial_recurrent, 900))
print(calculate_time(factorial_classic, 900))

