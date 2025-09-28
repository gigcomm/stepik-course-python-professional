import re

word = input().strip()
text = input().strip()

if word.lower().endswith('ze'):
    alt_word = word[:-2] + 'se'
elif word.lower().endswith('se'):
    alt_word = word[:-2] + 'ze'
else:
    alt_word = word.lower()

pattern = rf'\b{word.lower()}|{alt_word}\b'
match = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(match))