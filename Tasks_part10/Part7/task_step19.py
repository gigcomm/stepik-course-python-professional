def unique(iterable):
    seen = set()
    for item in iterable:
        if item not in seen:
            seen.add(item)
            yield item


numbers = [1, 2, 2, 3, 4, 5, 5, 5]
print(*unique(numbers))
iterator = iter('111222333')
uniques = unique(iterator)
print(next(uniques))
print(next(uniques))
print(next(uniques))
