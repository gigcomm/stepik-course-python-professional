def pattern(word):
    pattern = [1 if ch in vowels else 0 for ch in word]
    if 1 in pattern:
        last_index_vowel = len(pattern) - 1 - pattern[::-1].index(1)
        pattern = pattern[:last_index_vowel]
    return pattern

vowels = "ауоыиэяюёе"

start_word = input().strip()
n = int(input())
words = [input().strip() for _ in range(n)]
pattern_start_word = pattern(start_word)

result_words = [word for word in words if pattern_start_word == pattern(word)]
for word in result_words:
    print(word)
