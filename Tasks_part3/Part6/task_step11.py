import time

time_to_funcs = []

def get_the_fastest_func(funcs, arg):
    if not funcs:
        return None

    for func in funcs:
        start_time = time.perf_counter()
        func(arg)
        end_time = time.perf_counter()
        time_to_funcs.append(end_time - start_time)

    index_min_time = time_to_funcs.index(min(time_to_funcs))
    return funcs[index_min_time]


# def get_the_fastest_func(funcs, arg):
#     fastest_func = None
#     min_time = float('inf')
#
#     for func in funcs:
#         start_time = time.perf_counter()
#         func(arg)
#         end_time = time.perf_counter()
#         execution_time = end_time - start_time
#
#         if execution_time < min_time:
#             min_time = execution_time
#             fastest_func = func
#
#     return fastest_func