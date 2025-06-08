from datetime import datetime

result = []
dates = input()
dates_list = [datetime.strptime(i, '%d.%m.%Y')for i in dates.split(' ')]
for i in range(len(dates_list)-1):
    delta = abs(dates_list[i]-dates_list[i+1])
    result.append(delta.days)
print(result)