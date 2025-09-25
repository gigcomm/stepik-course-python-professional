import re

regex = r'^\d{1,2}[A-Za-z]{3,}\.{0,3}$'

text = ("4rTur")

print(*re.findall(regex, text))
