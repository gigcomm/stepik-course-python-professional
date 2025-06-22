import calendar
from datetime import date


def get_days_in_month(year, month):
    num_month = list(calendar.month_name).index(month)
    last_day = calendar.monthrange(year, num_month)[1]

    return [date(year, num_month, day) for day in range(1, last_day+1)]

print(get_days_in_month(2008, "December"))
