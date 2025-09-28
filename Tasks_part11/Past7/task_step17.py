import re
import sys

html = sys.stdin.read()

# Находим все открывающие теги (без закрывающих </...>)
tags = re.findall(r'<([a-zA-Z0-9]+)([^>]*)>', html)

tag_attrs = {}

for tag, attrs in tags:
    # Инициализируем множество атрибутов
    tag_attrs.setdefault(tag, set())

    # Достаём имена атрибутов (то, что перед = )
    attr_names = re.findall(r'([a-zA-Z-]+)\s*=', attrs)
    for name in attr_names:
        tag_attrs[tag].add(name)

# Сортируем теги
for tag in sorted(tag_attrs):
    attrs = sorted(tag_attrs[tag])
    if attrs:
        print(f"{tag}: {', '.join(attrs)}")
    else:
        print(f"{tag}: ")
