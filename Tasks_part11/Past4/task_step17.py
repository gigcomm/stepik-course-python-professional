import re

regex = r'^[MED][rs][s\.]\.?[A-Za-z]*$'

text = ("Mr.Jones")

print(*re.findall(regex, text))
