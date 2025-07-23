import json
from json import JSONDecodeError
from json.decoder import JSONObject


def is_correct_json(str):
    try:
        json.loads(str)
        return True
    except (JSONDecodeError, TypeError):
        return False



data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'
print(is_correct_json(data))
