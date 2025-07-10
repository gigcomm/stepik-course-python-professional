import sys

data = sys.stdin.readlines()
filtered_lines = [line for line in data if not line.strip().startswith('#') and line.strip() != '']
print(''.join(filtered_lines), end='')