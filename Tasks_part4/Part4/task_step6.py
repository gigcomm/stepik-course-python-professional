import json
import sys


input_line = sys.stdin.read().strip()
# is_correct_json(input_line)

data = json.loads(input_line)

for key, value in data.items():
    if isinstance(value, list):
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}: {value}')
