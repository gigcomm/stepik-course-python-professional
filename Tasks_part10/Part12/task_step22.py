from itertools import product
n, m = int(input()), int(input())


digits = [str(i) for i in range(min(n, 10))] + [chr(ord('A') + i) for i in range(max(0, n -10))]
numbers = [''.join(p) for p in product(digits, repeat=m)]
print(*numbers)
