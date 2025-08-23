import sys
from collections import Counter

data = [line.strip().split() for line in sys.stdin if line.strip()]

words_count = Counter({name: int(grade) for name, grade in data})
print(words_count.most_common()[::-1][1][0])
