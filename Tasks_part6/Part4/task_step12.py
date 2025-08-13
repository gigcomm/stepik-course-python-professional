import csv
from collections import namedtuple
from datetime import datetime


Meeting = namedtuple('Meeting', ['surname', 'name', 'date', 'time'])

meetings = []
with open('meetings.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file, delimiter=',')
    for row in reader:
        meeting = Meeting(
            surname=row['surname'],
            name=row['name'],
            date=row['meeting_date'],
            time=row['meeting_time']
        )
        meetings.append(meeting)

def get_sort_key(meeting):
    return datetime.strptime(f"{meeting.date} {meeting.time}", '%d.%m.%Y %H:%M')

meetings_sorted = sorted(meetings, key=get_sort_key)
for meeting in meetings_sorted:
    print(meeting.surname, meeting.name)
