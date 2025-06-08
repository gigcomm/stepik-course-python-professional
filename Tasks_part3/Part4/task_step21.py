from datetime import timedelta, datetime


def fill_up_missing_dates(dates):
    dates = [datetime.strptime(i, "%d.%m.%Y") for i in dates]
    min_date = min(dates)
    max_date = max(dates)

    full_fill_up_dates = []

    delta = (max_date - min_date).days
    for i in range(delta+1):
        date = min_date + timedelta(days=i)
        full_fill_up_dates.append(datetime.strftime(date, "%d.%m.%Y"))

    return full_fill_up_dates




dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
print(fill_up_missing_dates(dates))