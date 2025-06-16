from collections import defaultdict
from datetime import datetime

n = int(input())

hb_counts = defaultdict(int)

for _ in range(n):
    *name_parts, hb_date = input().split()
    date_obj = datetime.strptime(hb_date, "%d.%m.%Y")
    hb_counts[date_obj] += 1

max_count = max(hb_counts.values())
correct_hb_dates = [date for date, count in hb_counts.items() if count == max_count]

for date in sorted(correct_hb_dates):
    print(date.strftime("%d.%m.%Y"))