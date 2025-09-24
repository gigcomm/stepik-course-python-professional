import re

regex = r'[1-3][0-2][12x][0-3aA][xsu][.,]'

text = "I got two strange combinations: 22xAu, 1010x."

print(*re.findall(regex, text))