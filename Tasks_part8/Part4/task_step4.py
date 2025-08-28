def recursive_sum(nested_lists):
    total = 0
    if isinstance(nested_lists, int):
        total += nested_lists
    else:
        for nested_list in nested_lists:
            total += recursive_sum(nested_list)

    return total

my_list = [1, [4, 4], 2, [1, [2, 10]]]
print(recursive_sum(my_list))