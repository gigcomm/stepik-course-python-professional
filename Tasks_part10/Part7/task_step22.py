def pairwise(iterable):
    iterator = iter(iterable)
    next_item = next(iterator)

    for item in iterator:
        yield next_item, item
        next_item = item

    yield next_item, None




numbers = [1, 2, 3, 4, 5]
print(*pairwise(numbers))

iterator = iter('stepik')
print(*pairwise(iterator))