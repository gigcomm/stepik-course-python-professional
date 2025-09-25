import re

regex = r'((\d{3}|\(\d{3}\))[-\s]\d{3}-\d{4})'

text = ("Badeline: (810)-555-1234")
print(*re.findall(regex, text))
