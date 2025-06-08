import datetime


def num_of_sundays(year: int):
    count = 0
    for month in range(1, 13):
        for day in range(1, 32):
            try:
                current_date = datetime.date(year, month, day)
                if current_date.weekday() == 6:
                    count += 1
            except ValueError:
                continue
    return count

year = 2023
print(num_of_sundays(year))


