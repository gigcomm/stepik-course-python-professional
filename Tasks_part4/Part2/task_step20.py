import csv
from collections import defaultdict


def condense_csv(filename, id_name='id'):
    data = defaultdict(dict)
    field_order = []
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        for obj, prop, value in reader:
            data[obj][prop] = value
            if prop not in field_order:
                field_order.append(prop)

    with open('condensed.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id_name] + field_order)
        for obj in data:
            row = [obj] + [data[obj].get(prop, '') for prop in field_order]
            writer.writerow(row)

condense_csv('data1.csv', 'id')