import calendar
import datetime
from datetime import date


def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        max_day_month = calendar.monthrange(year, month)[1]
        for day in range(1, max_day_month+1):
            d = date(year, month, day)
            if d.weekday() == 0:
                mondays.append(d)
    return mondays

print(get_all_mondays(2008))

#Быстрее
# def get_all_mondays(year):
#     return [
#         datetime.date(year, month, day)
#         for month in range(1, 13)
#         for day in range(1, calendar.monthrange(year, month)[1] + 1)
#         if datetime.date(year, month, day).weekday() == 0
#     ]