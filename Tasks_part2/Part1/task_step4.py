def hide_card(card_number):
    digits = card_number.replace(' ','')
    return '*' * 12 + digits[-4:]

print(hide_card('905 678123 45612 56'))
