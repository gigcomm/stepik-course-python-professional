import re

regex = r'\b[A-Z]+\b'

text = ("I will go to the shop aNd you stay At home")

print(*re.findall(regex, text))
