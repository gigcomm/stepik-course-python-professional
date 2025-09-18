def with_previous(iterable):
    prev = None
    for item in iterable:
        yield prev, item
        prev = item

numbers = [1, 2, 3, 4, 5]
print(*with_previous(numbers))

iterator = iter('stepik')
print(*with_previous(iterator))