from collections import ChainMap


def deep_update(chainmap, key, value):
    for dictionary in chainmap.maps:
        if key in dictionary:
            dictionary[key] = value
    if key not in chainmap:
        chainmap.maps[0][key] = value


chainmap = ChainMap({'city': 'Moscow'}, {'name': 'Arthur'}, {'name': 'Timur'})
deep_update(chainmap, 'name', 'Dima')
print(chainmap)
