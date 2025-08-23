from collections import Counter


def scrabble(symbols, word):
    symbl = Counter(symbols.lower())
    word = Counter(word.lower())
    return (symbl & word) == word


print(scrabble('bbbbbeeeeegggggggeeeeeekkkkk', 'Beegeek'))