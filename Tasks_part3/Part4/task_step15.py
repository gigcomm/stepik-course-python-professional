from datetime import datetime, timedelta

d = input()
date_input = datetime.strptime(d, "%d.%m.%Y").date()
print(date_input-timedelta(days=1), date_input+timedelta(days=1), sep='\n')