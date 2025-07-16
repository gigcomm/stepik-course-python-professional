import csv
file = open('grades.csv', encoding='utf-8')
rows = csv.DictReader(file, delimiter=';')
for row in rows:
    if row['old_price'] > row['new_price']:
        print(row)