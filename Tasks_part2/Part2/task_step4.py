from collections import Counter

numbers_str = input().split()

counter = Counter(numbers_str)

duplicates = filter(lambda x: counter[x]>1, counter)
print(*sorted(duplicates))