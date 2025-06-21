import calendar
n = int(input())
years = [int(input()) for _ in range(n)]

for year in years:
    print(calendar.isleap(year))

