import time


def for_and_append(iterable):
    result = []
    for elem in iterable:
        result.append(elem)
    return result

def list_comprehension(iterable):
    return [elem for elem in iterable]

def list_function(iterable):
    return list(iterable)

def calculate_time(func, iterable):
    start_time = time.perf_counter()
    func(iterable)
    end_time = time.perf_counter()
    return end_time - start_time

print(calculate_time(for_and_append, range(100_000)))
print(calculate_time(list_comprehension, range(100_000)))
print(calculate_time(list_function, range(100_000)))