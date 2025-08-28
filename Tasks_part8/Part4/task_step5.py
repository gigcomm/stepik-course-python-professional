def linear(nested_lists):
    result = []
    if isinstance(nested_lists, list):
        for nested_list in nested_lists:
            result.extend(linear(nested_list))
    else:
        result.append(nested_lists)

    return result

my_list = [3, [4], [5, [6, [7, 8]]]]
print(linear(my_list))