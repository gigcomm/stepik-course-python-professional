import time

def calculate_it(func, *args):
    start_time = time.perf_counter()
    res_func = func(*args)
    end_time = time.perf_counter()
    time_work_func = end_time - start_time
    return (res_func, time_work_func)

# def add(a, b, c):
#     time.sleep(3)
#     return a + b + c
#
# print(calculate_it(add, 1, 2, 3))