import re

regex = r'[a-z][0-9][a-z][A-Z][A-Z]'

text = "My name is t1mUR and I am a1iVE!"

print(*re.findall(regex, text))