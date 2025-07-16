import csv
from collections import defaultdict

manager_dict = defaultdict(lambda: [0, 0])
with open("salary_data.csv", 'r', encoding="UTF-8", newline='') as file:
    rows = csv.DictReader(file, delimiter=';')
    for row in rows:
          company = row['company_name']
          salary = int(row['salary'])
          manager_dict[company][0] += salary
          manager_dict[company][1] += 1

averages = [(company, total/count) for company, (total, count) in manager_dict.items()]

averages.sort(key=lambda item: (item[1], item[0]))

for company, _ in averages:
    print(company)
