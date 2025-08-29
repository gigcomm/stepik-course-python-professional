def get_all_values(nested_dicts, key):
    result = set()
    if key in nested_dicts:
        result.add(nested_dicts[key])

    for nested_dict, val in nested_dicts.items():
        if isinstance(val, dict):
            val = get_all_values(val, key)
            if val is not None:
                result |= val
    return result

my_dict = {'users': {'Arthur': {'grades': [4, 4, 3], 'top_grade': 4}, 'Timur':
{'grades': [5, 5, 5], 'top_grade': 5}}}
result = get_all_values(my_dict, 'top_grade')
print(*sorted(result))