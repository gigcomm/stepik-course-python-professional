import re

regex = r'(\d{5}(-\d{4})?)'

text = ("New postcode: 09090-8989, old postcode 0909-8989")
matches = re.findall(regex, text)

# Берём только полные совпадения (первый элемент каждого кортежа)
print(*[m[0] for m in matches])
