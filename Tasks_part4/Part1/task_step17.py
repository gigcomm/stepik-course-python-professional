import datetime
import sys

dates = [datetime.datetime.strptime(line.strip(), "%d.%m.%Y") for line in sys.stdin]
if len(dates) < 2:
    sys.stdout.write("MIX")
else:
    asc_sorted = sorted(dates)
    desc_sorted = sorted(dates, reverse=True)
    # is_asc = all(dates[i] <= dates[i + 1] for i in range(len(dates) - 1))
    # is_desc = all(dates[i] >= dates[i + 1] for i in range(len(dates) - 1))

    if asc_sorted == dates:
        sys.stdout.write("ASC")
    elif dates == desc_sorted:
        sys.stdout.write("DESC")
    else:
        sys.stdout.write("MIX")