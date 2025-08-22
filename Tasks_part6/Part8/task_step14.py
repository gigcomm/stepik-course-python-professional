from collections import Counter


words = input().lower().split()
words_count = Counter(words)

if words_count:
    max_words = max(words_count.values())
    rare_words = [word for word, count in words_count.items() if count==max_words]

    if len(rare_words) > 1:
        result = max(rare_words)
        print(result)
    else:
        print(rare_words[0])
