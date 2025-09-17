def cubes_of_odds(obj):
    return (item ** 3 for item in obj if item % 2 == 1)

evens = [2, 4, 6, 8, 10]
print(list(cubes_of_odds(evens)))