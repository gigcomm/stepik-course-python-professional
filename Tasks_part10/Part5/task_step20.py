def card_deck(suit):
    nominal_cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['пик', 'треф', 'бубен', 'червей']

    filtered_suits = [s for s in suits if s != suit]

    while True:
        for suit in filtered_suits:
            for card in nominal_cards:
                yield f"{card} {suit}"


generator = card_deck('треф')
cards = [next(generator) for _ in range(40)]
print(*cards)
