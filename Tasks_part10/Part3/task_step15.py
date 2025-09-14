
def is_iterator(obj):
    if obj == iter(obj):
        return True
    return False

beegeek = map(str.upper, 'beegeek')
print(is_iterator(beegeek))

