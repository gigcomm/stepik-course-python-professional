import csv

male_names = []
female_names = []
with open('titanic.csv', 'r', encoding='utf-8', newline='') as file:
    data = csv.DictReader(file, delimiter=';')
    for d in data:
        if d['survived'] == '1' and float(d['age']) < 18 and d['age']:
            if d['sex'] == 'male':
                male_names.append(d['name'])
            elif d['sex'] == 'female':
                female_names.append(d['name'])

for name in male_names + female_names:
    print(name)



