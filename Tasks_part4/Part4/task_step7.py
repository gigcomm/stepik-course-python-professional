import json

with open('data1.json', 'r', encoding='utf-8') as file:
    data = json.load(file)


result = []
for value in data:
    if isinstance(value, str):
        result.append(value + '!')
    elif isinstance(value, int) or isinstance(value, float):
        result.append(value+1)
    elif isinstance(value, bool):
        result.append(not value)
    elif isinstance(value, list):
        result.append(value*2)
    elif isinstance(value, dict):
        value['newkey'] = None
        result.append(value)
    elif value is None:
        continue

with open("update_data.json", 'w', encoding="utf-8") as file:
    json.dump(result, file, ensure_ascii=False)
