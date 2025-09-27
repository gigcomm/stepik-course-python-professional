import re
import sys

count = 0

for line in sys.stdin:
    line = line.rstrip()
    if re.search('beegeek', line, re.IGNORECASE):
        count += 1

print(count)