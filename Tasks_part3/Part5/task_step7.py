from datetime import datetime, timedelta

date_today = input()
date_today_f = datetime.strptime(date_today, "%d.%m.%Y").date()

birthday_dates = dict()

n = int(input())
for _ in range(n):
    *name_parts, hb_date = input().split()
    date_obj = datetime.strptime(hb_date, "%d.%m.%Y")
    birthday_dates[date_obj] = name_parts

date_end = date_today_f + timedelta(days=7)

upcoming_birthday = {}

for hb_date, name_parts in birthday_dates.items():
    this_year_hb = hb_date.replace(year=date_today_f.year)
    if this_year_hb < date_today_f:
        this_year_hb = this_year_hb.replace(year=this_year_hb.year + 1)

    if date_today_f < hb_date <= date_end:
        upcoming_birthday[hb_date] = name_parts

if upcoming_birthday:
    youngest_date = max(upcoming_birthday.keys())
    print(upcoming_birthday[youngest_date])
else:
    print("Дни рождения не планируются")



