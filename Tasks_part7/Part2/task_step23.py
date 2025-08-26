import sys

num_count = 0
not_num_count = 0

for line in sys.stdin:
    value = line.strip()
    try:
        num_count += float(value)
    except ValueError:
        not_num_count += 1

print(num_count, not_num_count, sep='\n')
