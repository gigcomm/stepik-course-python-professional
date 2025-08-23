from collections import Counter

books = list(map(int, input().split()))
inventory = Counter(books)

n = int(input())

total_income = 0

for _ in range(n):
    cls, price = map(int, input().split())
    if inventory[cls] > 0:
        total_income += price
        inventory[cls] -= 1

print(total_income)
