import csv
import json
from collections import Counter

# Загружаем цены
with open('prices.json', encoding='utf-8') as f:
    prices = json.load(f)

quarters = ['quarter1.csv', 'quarter2.csv', 'quarter3.csv', 'quarter4.csv']

total_quantities = Counter()

for file in quarters:
    with open(file, encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        # создаём Counter для текущего квартала
        quarter_counter = Counter({
            row['продукт']: sum(int(row[month]) for month in row if month != 'продукт')
            for row in reader
        })
        # суммируем с общим Counter через +
        total_quantities += quarter_counter

# итоговый доход
total_income = sum(total_quantities[product] * prices[product] for product in total_quantities)

print(total_income)