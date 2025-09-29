import re

text = input().strip()
#text = " bee,geek . Python   ,  C++"

result = re.split(r'\s*[.,;]\s*', text)
print(*result)