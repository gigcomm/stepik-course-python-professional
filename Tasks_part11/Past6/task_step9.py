import sys
from re import search

for line in sys.stdin:
    line = line.strip()
    match = search(r"(\d{1,3})[- ](\d{1,3})[- ](\d{4,10})", line)
    country_code, city_code, number = match.groups()
    print(f"Код страны: {country_code}, Код города: {city_code}, Номер: {number}")
