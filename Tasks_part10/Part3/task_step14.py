def is_iterable(obj):
    try:
        iter(obj)
    except TypeError:
        return False
    else:
        return True

print(is_iterable('18731'))
