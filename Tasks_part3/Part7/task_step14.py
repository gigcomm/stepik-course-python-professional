import calendar
import datetime
from datetime import date


def free_day_museum_Ermitage(year):
    free_days = []
    for month in range(1, 13):
        thursdays = [week[3] for week in calendar.monthcalendar(year, month) if week[3] != 0]
        free_days.append(date(year, month, thursdays[2]))
    return free_days


for day in free_day_museum_Ermitage(2021):
    print(day.strftime('%d.%m.%Y'))


# def free_day_museum_Ermitage(year):
#     return [datetime.date(year, month, [w[3] for w in calendar.monthcalendar(year, month) if w[3] != 0][2])
#             for month in range(1, 13)
#             ]
#print('\n'.join(day.strftime('%d.%m.%Y') for day in free_day_museum_Ermitage(2021)))