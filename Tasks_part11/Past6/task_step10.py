import sys
import re

for line in sys.stdin:
    line = line.strip()
    match = re.fullmatch(r'_\d+\w*_?', line)
    if match:
        print(True)
    else:
        print(False)