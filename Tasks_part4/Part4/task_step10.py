import json

with open('countries.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

new_data = dict()
for d in data:
    country = d['country']
    religion = d['religion']

    if religion not in new_data:
        new_data[religion] = []

    new_data[religion].append(country)


with open('religion.json', 'w', encoding='utf-8') as file:
    data = json.dump(new_data, file, ensure_ascii=False)
