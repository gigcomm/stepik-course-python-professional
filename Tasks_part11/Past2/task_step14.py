import re

regex = r'ca[rtb]'

text =  "Cart carcat caBriolet Cabriolet cabriolet"

print(*re.findall(regex, text))