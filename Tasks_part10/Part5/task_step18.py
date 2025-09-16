def reverse(sequence):
    for i in reversed(sequence):
        yield i

generator = reverse('beegeek')
print(type(generator))
print(*generator)