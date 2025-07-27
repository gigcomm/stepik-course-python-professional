import csv
import json


with open('students.json', 'r', encoding='utf-8') as file:
    students = json.load(file)


filtered_students = [
    {'name': student['name'], 'phone': student['phone']}
    for student in students
    if student['age'] >= 18 and student['progress'] >= 75
]

filtered_students.sort(key=lambda x: x['name'])


with open('data.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['name', 'phone'], delimiter=',')
    writer.writeheader()
    writer.writerows(filtered_students)
