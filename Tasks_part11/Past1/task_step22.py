import re

regex = r'...\....'

text = ("I read the letter.Stood up.Sat down.Pondered for a minute."
        "Then reread the letter again.")

print(*re.findall(regex, text))