import csv


def parse_class_name(name):
    number, letter = name.split('-')
    return (int(number), letter)


with open('student_counts.csv', 'r', encoding='utf-8', newline='') as file:
    reader = csv.DictReader(file, delimiter=',')
    rows = list(reader)
    year = ['year']
    fieldnames = reader.fieldnames

    class_column = sorted(fieldnames[1:], key=parse_class_name)

    sorted_fieldnames = year + class_column

    with open('sorted_student_counts.csv', 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=sorted_fieldnames, delimiter=',')
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
