from collections import Counter

text = input().split()

first_occurrence = {}
for i, word in enumerate(text):
    length = len(word)
    if length not in first_occurrence:
        first_occurrence[length] = i

words_count = Counter(len(word) for word in text)
groups = [(length, count, first_occurrence[length]) for length, count in words_count.items()]

for length, count, _ in sorted(groups, key=lambda x: (x[1], x[2])):
    print(f"Слов длины {length}: {count}")