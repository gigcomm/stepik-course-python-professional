import re

text = input().strip()

res = re.sub(r'\b(\w)(\w)', r'\g<2>\g<1>', text)
print(res)
#This is Python
