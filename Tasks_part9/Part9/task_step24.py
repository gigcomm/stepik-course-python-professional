import sys
from functools import lru_cache


@lru_cache(maxsize=1000)
def cached_sort(word):
    return ''.join(sorted(word))

result = []
for line in sys.stdin:
    word = line.strip()
    result.append(cached_sort(word))

print('\n'.join(result))