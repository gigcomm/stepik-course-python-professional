from collections import Counter

products = input().split(',')
count_products = Counter(products)
for name, count in sorted(count_products.items()):
    print(f"{name}: {count}")