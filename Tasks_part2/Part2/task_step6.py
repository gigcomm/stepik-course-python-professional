n = int(input())

common_language = None

for _ in range(n):
    languages = set(input().split(', '))
    if common_language is None:
        common_language = languages
    else:
        common_language &= languages

if common_language:
    for language in common_language:
        print(language)
else: print("Сериал не состоится")