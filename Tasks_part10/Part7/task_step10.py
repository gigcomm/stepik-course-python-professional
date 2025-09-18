import datetime


def years_days(year):
    date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)

    while date < end_date:
        yield date
        date += datetime.timedelta(days=1)


dates = years_days(2022)
print(next(dates))
print(next(dates))
print(next(dates))
print(next(dates))
