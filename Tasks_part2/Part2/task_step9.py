from collections import defaultdict

units_in_bytes = {
    "B": 1,
    "KB": 1024,
    "MB": 1024 ** 2,
    "GB": 1024 ** 3
}

unit_order = ["B", "KB", "MB", "GB"]


# Функция для перевода байт в максимально возможную единицу с округлением
def format_size(total_bytes):
    for i in reversed(range(len(unit_order))):
        unit = unit_order[i]
        if total_bytes >= units_in_bytes[unit]:
            value = total_bytes / units_in_bytes[unit]
            return f"{round(value)} {unit}"
    return f"{total_bytes} B"


groups = defaultdict(list)
sizes = defaultdict(int)

with open("file.txt", "r", encoding="UTF-8") as f:
    for line in f:
        name, size_str, unit = line.strip().split()
        size = int(size_str)
        size_in_bytes = size * units_in_bytes[unit]

        ext = name.split('.')[-1]
        groups[ext].append(name)
        sizes[ext] += size_in_bytes

for ext in sorted(groups.keys()):
    for filename in sorted(groups[ext]):
        print(filename)
    print('-----------')
    print(f'Summary: {format_size(sizes[ext])}\n')
