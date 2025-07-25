import json


with open('data_1.json', 'r', encoding='utf-8') as file:
    data1 = json.load(file)

with open('data_2.json', 'r', encoding='utf-8') as file:
    data2 = json.load(file)

result = data1 | data2

with open('data_merge.json', 'w', encoding='utf-8') as file:
    json.dump(result, file)
