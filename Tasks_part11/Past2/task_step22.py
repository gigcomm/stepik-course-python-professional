import re

regex = r'[01][0-9]:[0-5][0-9]|2[0-3]:[0-5][0-9]'

text = "So why does my watch say 91:44? It doesn't matter, I'll be there at 17:30 00:00, 00:60, 24:00, 50:39, 17/30"

print(*re.findall(regex, text))