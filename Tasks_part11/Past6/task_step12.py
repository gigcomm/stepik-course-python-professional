import sys
from re import search

count_bee = 0
count_geek = 0

for line in sys.stdin:
    line = line.strip()
    first = search(r'bee', line)
    if first:
        second = search(r'bee', line[first.end():])
        if second:
            count_bee += 1
    if search(r'\bgeek\b', line):
        count_geek += 1


print(count_bee)
print(count_geek)
