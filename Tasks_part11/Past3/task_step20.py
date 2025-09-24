import re

regex = r'[A-Z]{1,2}\d[0-9A-Z]?\s\d[^CIKMOV]{2}'

text = "Our postcodes. Arthur: NW11 8AB, Timur: P01 3AX, Anri: H7Z9T4 Dima: N16 6PS"

print(*re.findall(regex, text))