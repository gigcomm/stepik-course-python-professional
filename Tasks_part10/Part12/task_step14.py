from collections import namedtuple
import itertools

Item = namedtuple('Item', ['name', 'mass', 'price'])

items = [Item('Обручальное кольцо', 7, 49_000),
         Item('Мобильный телефон', 200, 110_000),
         Item('Ноутбук', 2000, 150_000),
         Item('Ручка Паркер', 20, 37_000),
         Item('Статуэтка Оскар', 4000, 28_000),
         Item('Наушники', 150, 11_000),
         Item('Гитара', 1500, 32_000),
         Item('Золотая монета', 8, 140_000),
         Item('Фотоаппарат', 720, 79_000),
         Item('Лимитированные кроссовки', 300, 80_000)]

capacity = int(input())

best_value = 0
best_combination = []

for r in range(1, len(items) + 1):
    for comb in itertools.combinations(items, r):
        total_mass = sum(i.mass for i in comb)
        total_price = sum(i.price for i in comb)
        if total_mass <= capacity and total_price > best_value:
            best_value = total_price
            best_combination = comb

if best_combination:
    for item in sorted(best_combination, key=lambda i: i.name):
        print(item.name)
else:
    print('Рюкзак собрать не удастся')

