import time


def for_and_append():
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result


def list_comprehension():
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]

def calculate_time(func):
    start_time = time.perf_counter()
    func()
    end_time = time.perf_counter()
    return end_time - start_time

print(calculate_time(func=for_and_append))
print(calculate_time(func=list_comprehension))
