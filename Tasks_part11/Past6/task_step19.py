import re

s = input().strip()

start_words = ['Здравствуйте', 'Доброе утро', 'Добрый день', 'Добрый вечер']

for word in start_words:
    if re.search(word, s, re.IGNORECASE | re.MULTILINE):
        print(True)
        break
else:
    print(False)
