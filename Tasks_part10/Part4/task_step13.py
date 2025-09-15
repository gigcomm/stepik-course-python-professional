class CardDeck:
    def __init__(self):
        self.cards_numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10','J', 'Q', 'K', 'A']
        self.suits = ['пик', 'треф', 'бубен', 'червей']
        self.index_nums = 0
        self.index_suits = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index_suits >= len(self.suits):
            raise StopIteration

        card = f"{self.cards_numbers[self.index_nums]} {self.suits[self.index_suits]}"

        self.index_nums += 1
        if self.index_nums >= len(self.cards_numbers):
            self.index_suits += 1
            self.index_nums = 0

        return card


cards = CardDeck()
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
print(next(cards))
