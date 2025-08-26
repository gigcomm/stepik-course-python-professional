def get_id(names, name):
    if not isinstance(name, str):
        raise TypeError('Имя не является строкой')
    if not(name.isalpha() and name[0].isupper() and not name[1:].islower()):
        raise ValueError('Имя не является корректным')

    return len(names) + 1

names = ['Timur', 'Anri', 'Dima', 'Arthur', 'Ruslan']
name = ['E', 'd', 'u', 'a', 'r', 'd']
try:
    print(get_id(names, name))
except TypeError as e:
    print(e)