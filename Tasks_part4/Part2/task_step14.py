import csv


def csv_columns(filename):
    data = {}
    with open(filename, 'r', encoding='utf-8', newline='') as file:
        rows = csv.DictReader(file, delimiter=',')
        for field in rows.fieldnames:
            data[field] = []

        for row in rows:
            for key in row:
                data[key].append(row[key])

    return data


data = csv_columns("exam.csv")
print(data)
