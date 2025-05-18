def choose_plural(amount, declensions):
    if 11 <= amount % 100 <= 14:
        return f"{amount} {declensions[2]}"
    elif amount % 10 == 1:
        return f"{amount} {declensions[0]}"
    elif 2 <= amount % 10 <= 4:
        f"{amount} {declensions[1]}"
    else:
        f"{amount} {declensions[2]}"


print(choose_plural(111, ('гвоздь', 'гвоздя', 'гвоздей')))
