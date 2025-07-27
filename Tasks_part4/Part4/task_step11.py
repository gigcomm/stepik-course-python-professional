import csv
import json

result = {}

with open('playgrounds.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=';')
    for d in data:
        adm_area = d['AdmArea']
        district = d['District']
        address = d['Address']

        if adm_area not in result:
            result[adm_area] = {}
        if district not in result[adm_area]:
            result[adm_area][district] = []

        result[adm_area][district].append(address)

with open('addresses.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, ensure_ascii=False, indent=3)
