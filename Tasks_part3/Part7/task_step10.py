import calendar

year, num_month = map(int, input().split())
print(calendar.monthrange(year, num_month)[1])
