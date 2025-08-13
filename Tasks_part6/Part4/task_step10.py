import pickle
from collections import namedtuple

Animal = namedtuple('Animal', ['name', 'family', 'sex', 'color'])

with open('data.pkl', mode='rb') as file:
    data = pickle.load(file)

for value in data:
    print(f'name: {value.name}\n'
          f'family: {value.family}'
          f'sex: {value.sex}\n'
          f'color: {value.color}\n')
    print()

