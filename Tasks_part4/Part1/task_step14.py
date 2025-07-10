import sys

count_strings = 0

for line in sys.stdin:
    stripped_line = line.strip()
    if stripped_line.startswith('#') or not stripped_line:
        count_strings += 1

print(count_strings)

