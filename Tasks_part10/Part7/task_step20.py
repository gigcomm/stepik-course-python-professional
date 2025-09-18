def stop_on(iterable, obj):
    for item in iterable:
        if obj == item:
            return
        yield item


iterator = iter('beegeek')
print(*stop_on(iterator, 'a'))
