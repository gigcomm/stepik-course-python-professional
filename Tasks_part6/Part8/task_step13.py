from collections import Counter

words = input().lower().split(' ')
words_count = Counter(words)

if words_count:
    min_words = min(words_count.values())
    rare_words = [word for word, count in words_count.items() if count==min_words]
    rare_words.sort()

    print(', '.join(rare_words))