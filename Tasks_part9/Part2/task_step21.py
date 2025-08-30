import sys

forms = max([eval(line) for line in sys.stdin if line.strip()])
print(forms)