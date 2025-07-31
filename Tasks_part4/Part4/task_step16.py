import json

result = {}

with open('food_services.json', 'r', encoding='utf-8') as file:
    foods = json.load(file)

for food in foods:
    name = food['Name']
    type_object = food['TypeObject']
    seats_count = food['SeatsCount']
    if type_object not in result or seats_count > result[type_object]['SeatsCount']:
        result[type_object] = {
            'Name': name,
            'SeatsCount': seats_count
        }

for type in sorted(result.keys()):
    info = result[type]
    print(f"{type}: {info['Name']}, {info['SeatsCount']}")
