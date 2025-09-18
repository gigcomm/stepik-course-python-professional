import csv


with open('data.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, delimiter=',')

    filtered_rows = (row for row in reader if row['round'] == 'a')
    amounts = (int(row['raisedAmt']) for row in filtered_rows)
    sums = sum(amounts)

print(sums)

