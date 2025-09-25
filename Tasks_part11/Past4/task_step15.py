import re

regex = r'^[A-Za-z]*s$'

text = ("Chess")

print(*re.findall(regex, text))
