def get_value(nested_dicts, key):
    if key in nested_dicts:
        return nested_dicts[key]

    for k, val in nested_dicts.items():
        if isinstance(val, dict):
            val = get_value(val, key)
            if val is not None:
                return val

data = {'firstName': 'Тимур', 'lastName': 'Гуев', 'birthDate': {'day': 10,
'month': 'October', 'year': 1993}, 'address': {'streetAddress': 'Часовая 25, кв. 127', 'city':
    {'region': 'Московская область', 'type': 'город', 'cityName': 'Москва'}, 'postalCode': '125315'}}

print(get_value(data, 'cityName'))