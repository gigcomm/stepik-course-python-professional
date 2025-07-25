import json

with open('people.json', 'r', encoding='utf-8') as file:
    people = json.load(file)

all_keys = set()
for person in people:
    all_keys.update(person.keys())

for person in people:
    for key in all_keys:
        if key not in person:
            person[key] = None


with open('update_json.json', 'w', encoding='utf-8') as file:
    json.dump(people, file)