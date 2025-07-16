import csv


def sort_csv_column(number_column):
    with open('deniro.csv', 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(file, delimiter=',')
        rows = list(reader)

    sample_value = rows[0][number_column-1]
    is_numeric = sample_value.isdigit()

    def sort_key(row):
        value = row[number_column-1]
        return int(value) if is_numeric else value

    sorted_rows = sorted(rows, key=sort_key)

    for row in sorted_rows:
        print(','.join(row))


sort_csv_column(1)
