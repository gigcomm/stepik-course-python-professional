def polynom(x):
    result = x ** 2 + 1
    polynom.values.add(result)
    return result

polynom.values = set()
polynom(1)
polynom(2)
polynom(3)
print(*sorted(polynom.values))
