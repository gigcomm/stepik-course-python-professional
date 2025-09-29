import re

text = input().strip()
pattern = r"(\d+)\(([a-z]*)\)"
while re.search(pattern, text):
    text = re.sub(pattern, lambda m: int(m.group(1)) * m.group(2), text)

print(text)
