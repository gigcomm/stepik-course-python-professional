from collections import ChainMap


def get_all_values(chainmap: ChainMap, key):
    names = set()
    for dictionary in chainmap.maps:
        if key in dictionary:
            names.add(dictionary[key])

    return names


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
result = get_all_values(chainmap, 'name')
print(*sorted(result))
