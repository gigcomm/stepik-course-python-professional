def flatten(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten(item)
        else:
            yield item



generator = flatten([1, 2, 3, 4, 5, 6, 7])
print(*generator)
