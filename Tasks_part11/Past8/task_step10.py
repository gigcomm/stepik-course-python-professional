import re


def normalize_whitespace(string):
    res = re.sub(r'\s+', ' ', string)
    return res

print(normalize_whitespace('AAAA                A                AAAA'))
print(normalize_whitespace('Тут нет лишних пробелов'))
print(normalize_whitespace('Тут   н   е   т     л   и     шних пробелов     '))