from collections import ChainMap


def get_value(chainmap, key, from_left=True):
    if from_left:
        for dictionary in chainmap.maps:
            if key in dictionary:
                return dictionary[key]
        return None
    else:
        for dictionary in reversed(chainmap.maps):
            if key in dictionary:
                return dictionary[key]
        return None


chainmap = ChainMap({'name': 'Arthur'}, {'name': 'Timur'})
print(get_value(chainmap, 'age'))