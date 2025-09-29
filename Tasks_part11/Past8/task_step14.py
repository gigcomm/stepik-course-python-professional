import re

text = input().strip()

pattern = r'(\b\w+\b)(\W+\1\b)+'
res = re.sub(pattern, r'\1', text)
print(res)

#hi, hi, hi, hello, hello, HELLO, HELLO, HELLO, HELLO, hello!