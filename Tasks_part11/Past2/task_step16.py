import re

regex = r'[A-Za-z][0-9]{4}'

text = "Order 1: B938274, Order 2: T8372, Order 3: g883929"

print(*re.findall(regex, text))