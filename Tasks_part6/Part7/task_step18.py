from collections import Counter


products = input().split(',')

count_products = Counter(products)
max_length = max(len(product) for product in count_products.keys())

for product in sorted(count_products):
    price = sum(ord(ch) for ch in product)
    total_price = price * count_products[product]


    print(f"{product.ljust(max_length)}: {price} UC x {count_products[product]} = {total_price} UC")

