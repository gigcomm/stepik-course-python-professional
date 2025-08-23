import csv
from collections import Counter

with open("name_log.csv", 'r', encoding="utf-8", newline='') as file:
    info = csv.DictReader(file, delimiter=',')
    emails_and_useraname = [(row['email'], row['username']) for row in info]

counter_change_username = Counter()
for email, count in set(emails_and_useraname):
    counter_change_username[email] += 1

for email in sorted(counter_change_username):
    print(f"{email}: {counter_change_username[email]}")