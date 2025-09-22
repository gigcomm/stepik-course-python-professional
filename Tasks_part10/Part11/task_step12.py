from itertools import groupby

words = input().split()

grouped_words = groupby(sorted(words, key=len), key=len)
for length, words in grouped_words:
    print(f"{length} -> {', '.join(words)}")