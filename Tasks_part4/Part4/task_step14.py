import csv
import json
from datetime import datetime

students = {}

with open('exam_results.csv', 'r', encoding='utf-8') as file:
    data = csv.DictReader(file, delimiter=',')

    for d in data:
        name = d['name']
        surname = d['surname']
        score = int(d['score'])
        date_and_time = d['date_and_time']
        email = d['email']
        if email not in students:
            students[email] = {
                'name': name,
                'surname': surname,
                'best_score': score,
                'date_and_time': date_and_time,
                'email': email
            }
        else:
            if score < students[email]['best_score']:
                students[email]['best_score'] = score
                students[email]['date_and_time'] = date_and_time
            elif score == students[email]['best_score']:
                current_date = datetime.strptime(students[email]['date_and_time'], "%Y-%m-%d %H:%M:%S")
                new_date = datetime.strptime(date_and_time, "%Y-%m-%d %H:%M:%S")
                if new_date > current_date:
                    students[email]['date_and_time'] = date_and_time


sorted_students = sorted(students.values(), key=lambda x: x['email'])

with open('best_scores.json', 'w', encoding='utf-8') as file:
    json.dump(sorted_students, file, ensure_ascii=False, indent=3)

