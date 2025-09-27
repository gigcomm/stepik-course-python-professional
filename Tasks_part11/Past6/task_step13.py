import sys
from re import search, fullmatch, match

count_popular = 0

for line in sys.stdin:
    line = line.strip()
    if fullmatch(r'(beegeek).*(beegeek)', line):
        popular = 3
    elif match(r'beegeek', line) or search(r'beegeek$', line):
        popular = 2
    elif search(r'beegeek', line):
        popular = 1
    else:
        popular = 0

    count_popular += popular

print(count_popular)


