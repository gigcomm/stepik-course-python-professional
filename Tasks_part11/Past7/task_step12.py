import re

s = input().strip()
word = input().strip()
pattern = r'(\b)' + re.escape(word) + r'(\b)'
print(len(re.findall(pattern, s)))
