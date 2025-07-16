import csv
import datetime

logs = {}

with open('name_log.csv', 'r', encoding='utf-8', newline='') as file:
    rows = csv.DictReader(file, delimiter=',')
    for row in rows:
        email = row['email']
        current_date = datetime.datetime.strptime(row['dtime'], "%d/%m/%Y %H:%M")

        if email not in logs or current_date > datetime.datetime.strptime(logs[email]['dtime'], "%d/%m/%Y %H:%M"):
            logs[email] = row

sorted_logs = sorted(logs.values(), key=lambda x: x['email'])

with open('new_name_log.csv', 'w', encoding='utf-8', newline='') as file:
    fieldnames = ['username', 'email', 'dtime']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writeheader()
    writer.writerows(sorted_logs)
