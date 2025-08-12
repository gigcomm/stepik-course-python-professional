import zipfile
import os


def convert_size(size_bytes):
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size_bytes < 1024:
            return f"{size_bytes} {unit}"
        size_bytes = round(size_bytes / 1024)
    return f"{size_bytes} TB"


def print_structure(zip_name):
    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        # Собираем все элементы и их уровни вложенности
        items = []
        for file_info in zip_ref.infolist():
            path = file_info.filename
            depth = path.count('/')
            if path.endswith('/'):
                depth -= 1  # Это директория
            items.append((depth, path, file_info.file_size))

        # Сортируем по пути для правильного отображения структуры
        items.sort(key=lambda x: x[1])

        # Выводим структуру
        for depth, path, size in items:
            if path.endswith('/'):
                # Это директория
                dir_name = path.rstrip('/').split('/')[-1]
                print('  ' * depth + dir_name)
            else:
                # Это файл
                file_name = path.split('/')[-1]
                readable_size = convert_size(size)
                print('  ' * depth + f"{file_name} {readable_size}")


# Вызываем функцию для архива desktop.zip
print_structure('desktop.zip')