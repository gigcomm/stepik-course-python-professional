from collections import Counter

count_ch = Counter()

with open('pythonzen.txt', 'r', encoding='utf-8') as file:
    text = file.read()

letters = [ch.lower() for ch in text if ch.isalpha()]
count_ch = Counter(letters)

for letter, count in sorted(count_ch.items()):
    print(f"{letter}: {count}")