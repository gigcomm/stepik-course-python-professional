import json

json_file = input().strip()

try:
    with open(json_file) as json_file:
        data = json.load(json_file)
except FileNotFoundError:
    print('Файл не найден')
except json.JSONDecodeError:
    print('Ошибка при десериализации')


