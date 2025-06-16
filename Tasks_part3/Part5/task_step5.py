from datetime import datetime

n = int(input())

parsed = []
for _ in range(n):
    parts = input().strip().split()
    name = parts[0]
    last_name = parts[1]
    hb_date = datetime.strptime(parts[2], "%d.%m.%Y").date()
    parsed.append((hb_date, last_name, name))

oldest_date = min(data[0] for data in parsed)
count_oldest_dates = [data for data in parsed if data[0] == oldest_date]

date_str =oldest_date.strftime("%d.%m.%Y")
if len(count_oldest_dates) == 1:
    print(f"{date_str} {count_oldest_dates[0][1]} {count_oldest_dates[0][2]}")
else:
    print(f"{date_str} {len(count_oldest_dates)}")
