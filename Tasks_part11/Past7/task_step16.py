import re
import sys

html = sys.stdin.read()  # читаем весь ввод как строку

# Ищем все гиперссылки: (href="...") и содержимое между <a>...</a>
pattern = r'<a\s+[^>]*href="([^"]+)"[^>]*>(.*?)</a>'
links = re.findall(pattern, html, flags=re.DOTALL | re.IGNORECASE)

for href, text in links:
    # убираем лишние пробелы и переводы строк внутри текста
    text = text.strip()
    print(f"{href}, {text}")
