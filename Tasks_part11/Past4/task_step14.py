import re

regex = r'^\w{2,}[a-z]*[A-Z]*$'

text = ("51tePIK")

print(*re.findall(regex, text))
