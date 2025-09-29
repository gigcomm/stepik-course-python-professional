import re

a, b = map(int, input().split())
text = input().strip()
substring = text[a:b]

regex_obj = re.compile(r'\d+')
result = sum(int(x) for x in regex_obj.findall(substring))
print(result)