import json
from collections import ChainMap

with open('zoo.json', 'r', encoding='utf-8') as file:
    info = json.load(file)

animals = ChainMap(*info)
print(sum(animals.values()))