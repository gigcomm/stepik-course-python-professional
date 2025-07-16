import csv
from collections import defaultdict

count_zone_wifi = defaultdict(int)

with open("wifi.csv", 'r', encoding='utf-8', newline='') as file:
    data = csv.DictReader(file, delimiter=';')
    for d in data:
        count_zone_wifi[d['district']] += int(d['number_of_access_points'])

sorted_wifi_zone = sorted(count_zone_wifi.items(), key=lambda item: (item[1], item[0].lower()), reverse=True)
for rayon, count in sorted_wifi_zone:
    print(f'{rayon}: {count}')