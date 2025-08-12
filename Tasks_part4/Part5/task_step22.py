import zipfile
import json
import os

from Tasks_part4.Part4.task_step5 import is_correct_json


def process_archive(zip_name):
    arsenal_players = []

    with zipfile.ZipFile(zip_name, 'r') as zip_ref:
        for file_info in zip_ref.infolist():
            if file_info.filename.endswith('.json'):
                try:
                    with zip_ref.open(file_info) as json_file:
                        content = json_file.read().decode('utf-8')
                        if is_correct_json(content):
                            player = json.loads(content)
                            if player.get('team') == 'Arsenal':
                                name = f"{player['first_name']} {player['last_name']}"
                                arsenal_players.append((player['first_name'], player['last_name'], name))
                except (KeyError, UnicodeDecodeError, json.JSONDecodeError):
                    continue

    # Сортируем сначала по имени, затем по фамилии
    arsenal_players.sort(key=lambda x: (x[0], x[1]))

    for _, _, name in arsenal_players:
        print(name)


# Пример вызова функции
process_archive('data.zip')