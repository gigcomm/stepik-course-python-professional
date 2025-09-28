import re

word = input().strip()
text = input().strip()

word_low = word.lower()
if 'our' in word_low:
    alt_word = word_low.replace('our', 'or')
else:
    alt_word = word_low

pattern = rf'\b{word.lower()}|{alt_word}\b'
match = re.findall(pattern, text, flags=re.IGNORECASE)
print(len(match))

# Odour
# the odour coming out of the left over food was intolerable. Ammonia has a very
# pungent odor