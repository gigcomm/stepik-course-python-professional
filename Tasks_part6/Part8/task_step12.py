from collections import Counter

words = input().lower().split(' ')
words_count = Counter(words)
print(words_count.most_common(1)[0][0])

