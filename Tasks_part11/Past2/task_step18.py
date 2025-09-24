import re

regex = r'[0-9][aeiouy][^bcDF]\S[^AEIOUY][^.,]'

text = " What password do you prefer: 9ython or 4uTUMN?"

print(*re.findall(regex, text))