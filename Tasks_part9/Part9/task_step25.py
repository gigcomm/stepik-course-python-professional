from functools import lru_cache

@lru_cache(maxsize=None)
def ways(n: int) -> int:
    if n == 1:
        return 1
    if n == 2:
        return 1
    if n == 3:
        return 1
    if n == 4:
        return 2
    return ways(n - 1) + ways(n - 3) + ways(n - 4)


print(ways(2))
print(ways(3))
print(ways(4))
