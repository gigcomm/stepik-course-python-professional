import re

regex = r'\d{2}(-)?\d{2}\1?\d{2}\1?\d{2}'

text = ("Digits from 0 to 7: 01234567  Digits from 1 to 8 by groups: 12-34-56-78")
print([m.group(0) for m in re.finditer(regex, text)])