from itertools import product

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
digit = [1, 2, 3, 4, 5, 6, 7, 8]

result = (letter + str(digit) for letter, digit in product(letters, digit))
print(*result)
