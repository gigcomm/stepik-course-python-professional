def txt_to_dict():
    with open('planets.txt', 'r', encoding='utf-8') as file:
        content = file.read()
        planets = content.split('\n\n')
        for planet in planets:
            yield dict(line.split(' = ') for line in planet.split('\n') if line)


planets = txt_to_dict()
print(next(planets))
print(next(planets))
print(next(planets))