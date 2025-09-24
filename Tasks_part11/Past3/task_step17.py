import re

regex = r'[A-Z]{5}\d{4}[A-Z]'

text = "ample Input 1:The PAN (or PAN number) is a ten-character long alpha-numeric unique identifier. Example: AAAPZ1234C"

print(*re.findall(regex, text))