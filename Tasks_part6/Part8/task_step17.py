from collections import Counter

data = Counter({'j': 8, 'q': 8, 't': 1})

data.min_values = lambda: [(k, v) for k, v in data.items() if v == min(data.values())] if data else []
data.max_values = lambda: [(k, v) for k, v in data.items() if v == max(data.values())] if data else []

print(data.min_values())
print(data.max_values())
