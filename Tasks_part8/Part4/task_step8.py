def dict_travel(nested_dicts):
    def rec_travel(data, current_path):
        for key in sorted(data.keys()):
            val = data[key]
            new_path = f'{current_path}.{key}' if current_path else key

            if isinstance(val, dict):
                rec_travel(val, new_path)
            else:
                print(f'{new_path}: {val}')

    rec_travel(nested_dicts, '')


data = {'a': 1, 'b': {'c': 30, 'a': 10, 'b': 20}}
dict_travel(data)
