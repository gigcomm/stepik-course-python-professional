import re

regex = r'[0-9A-F]'

text = "a - 10, B - 11, c - 12, D - 13, E - 14, F - 15, G - 16"

print(*re.findall(regex, text))