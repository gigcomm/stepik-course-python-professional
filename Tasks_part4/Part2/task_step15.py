import csv
from collections import defaultdict

written_info = defaultdict(int)

with open('data.csv', 'r', encoding='utf-8', newline='') as file:
    dates = csv.DictReader(file, delimiter=',')
    for data in dates:
        domain = data['email'].split('@')[-1]
        written_info[domain] += 1

sorted_domain = sorted(written_info.items(), key=lambda item: (item[1], item[0].lower()))

with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_w:
    columns = ['domain', 'count']
    writer = csv.DictWriter(file_w, fieldnames=columns, delimiter=',', quoting=csv.QUOTE_NONE)
    writer.writeheader()
    for domain, count in sorted_domain:
        writer.writerow({'domain': domain, 'count': count})