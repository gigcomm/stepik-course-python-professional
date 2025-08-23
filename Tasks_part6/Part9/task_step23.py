from collections import ChainMap, Counter

order = input().split(',')

counter_order = Counter(order)


bread = {'булочка с кунжутом': 15, 'обычная булочка': 10, 'ржаная булочка': 15}
meat = {'куриный бифштекс': 50, 'говяжий бифштекс': 70, 'рыбный бифштекс': 40}
sauce = {'сливочно-чесночный': 15, 'кетчуп': 10, 'горчица': 10, 'барбекю': 15, 'чили': 15}
vegetables = {'лук': 10, 'салат': 15, 'помидор': 15, 'огурцы': 10}
toppings = {'сыр': 25, 'яйцо': 15, 'бекон': 30}

products = ChainMap(bread, meat, sauce, vegetables, toppings)

max_len = max(len(name) for name in counter_order)

lines = []
total_price = 0

for product in sorted(counter_order):
    count = counter_order[product]
    price = products[product] * count
    total_price += price
    lines.append(f"{product.ljust(max_len)} x {count}")

line_sep = '-' * max(len(line) for line in lines + [f'ИТОГ: {total_price}р'])

for line in lines:
    print(line.ljust(max_len))
print(line_sep)
print(f'ИТОГ: {total_price}р')


