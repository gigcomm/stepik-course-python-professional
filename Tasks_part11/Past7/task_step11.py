import re

s = input().strip()
word = input().strip()
pattern = r'(?<=\w)' + re.escape(word) + r'(?=\w)'
print(len(re.findall(pattern, s)))
