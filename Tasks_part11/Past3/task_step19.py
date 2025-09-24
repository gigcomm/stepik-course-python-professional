import re

regex = r'[a-z]{0,3}\d{2,8}[A-Z]{3,}'

text = " Dear citizen! Your old ID: tba44891AHH, your new ID: 781AHHGYT"

print(*re.findall(regex, text))