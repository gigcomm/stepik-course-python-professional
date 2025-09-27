import sys
from re import fullmatch

for line in sys.stdin:
    line = line.strip()
    match = fullmatch(r'(\w+)\1+', line)
    if match:
        print(match.group())