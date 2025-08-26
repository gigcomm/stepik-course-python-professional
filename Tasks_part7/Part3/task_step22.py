name_file = input()
try:
    with open(name_file, 'r', encoding='utf-8') as f:
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')
