import re

regex = r'.*\(.*\).*'

text = ("(41 + 9) * 2 = ? ")

print(*re.findall(regex, text))
