from datetime import datetime

with open("diary.txt", encoding="UTF-8") as file:
    content = file.read()

entries = content.strip().split('\n\n')


def get_datetime(entry):
    first_line = entry.splitlines()[0]
    return datetime.strptime(first_line, '%d.%m.%Y; %H:%M')


entries_with_dt = [(get_datetime(entry), entry) for entry in entries]

sorted_entries = sorted(entries_with_dt, key=lambda x: x[0])

for _, entry in sorted_entries:
    print(entry)
    print()
