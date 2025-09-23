import re

regex = r'\w{3}'

text = ("150 + 1000 = 1150")

print(*re.findall(regex, text))