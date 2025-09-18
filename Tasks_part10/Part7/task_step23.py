def around(iterable):
    prev = None
    iterator_obj = iter(iterable)
    item = next(iterator_obj, None)

    while item is not None:
        next_item = next(iterator_obj, None)
        yield prev, item, next_item
        prev, item = item, next_item


numbers = [1, 2, 3, 4, 5]
print(*around(numbers))

iterator = iter('hey')
print(*around(iterator))