import calendar
from datetime import datetime

date_str = input()
date_f = datetime.strptime(date_str, "%Y-%m-%d").weekday()
print(list(calendar.day_name)[date_f])

