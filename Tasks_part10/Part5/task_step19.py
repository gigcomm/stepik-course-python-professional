from datetime import date, datetime, timedelta


def dates(start, count=None):
    current = start
    if count is None:
        while True:
            yield current
            current += timedelta(days=1)

    else:
        for _ in range(count):
            yield current
            current += timedelta(days=1)


generator = dates(date(2022, 3, 8), 5)
print(*generator)