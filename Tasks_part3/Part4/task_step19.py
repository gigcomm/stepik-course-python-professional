from datetime import datetime, timedelta

d = input()

date_input = datetime.strptime(d, '%d.%m.%Y')

print(date_input.strftime('%d.%m.%Y'))
current_date = date_input
for i in range(1, 10):
    current_date += timedelta(days=i+1)
    print(current_date.strftime('%d.%m.%Y'))
