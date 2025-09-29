import re

text = input().strip()

result = re.split(r'\s*(?:and|or|[&|])\s*', text)
print(', '.join(result))
