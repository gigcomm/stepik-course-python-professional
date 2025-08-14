from collections import defaultdict


def wins(pairs):
    data = defaultdict(list)
    for name_win, name_lose in pairs:
        data[name_win].append(name_lose)
    return data

result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима',
'Артур')])
for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))