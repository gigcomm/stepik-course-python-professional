import sys
data = [line.rstrip()[::-1] for line in sys.stdin]
for line in data:
    print(line)