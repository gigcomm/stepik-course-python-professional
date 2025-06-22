import calendar

year, name_month = input().split()
num_month = list(calendar.month_name).index(name_month)
print(calendar.monthrange(int(year), num_month)[1])