from itertools import groupby


def group_anagrams(words):
    grouped = groupby(sorted(words, key=lambda t: sorted(t)), key=lambda t: sorted(t))
    return [tuple(group) for _, group in grouped]

groups = group_anagrams(['evil', 'father', 'live', 'levi', 'book', 'afther',
'boko'])
print(*groups)

groups = group_anagrams(['evil', 'father', 'book', 'stepik', 'beegeek'])
print(*groups)

groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка',
'норка', 'чулки'])
print(*groups)