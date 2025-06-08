from datetime import datetime


def parse_date(date_entry):
    if '-' in date_entry:
        start_date, end_date = date_entry.split('-')
    else:
        start_date = end_date = date_entry

    start_date = datetime.strptime(start_date, '%d.%m.%Y').date()
    end_date = datetime.strptime(end_date, '%d.%m.%Y').date()

    start_ord = start_date.toordinal()
    end_ord = end_date.toordinal()

    return {datetime.fromordinal(i).date() for i in range(start_ord, end_ord + 1)}


def is_available_date(booked_dates, date_for_booking):
    booked_set = set()
    for entry in booked_dates:
        booked_set |= parse_date(entry)

    booking_set = parse_date(date_for_booking)
    return booking_set.isdisjoint(booking_set)