from datetime import datetime, timedelta

t = input()

time_input = datetime.strptime(t, '%H:%M:%S')
midnight = time_input.replace(hour=0, minute=0, second=0)
delta = time_input - midnight
print(int(delta.total_seconds()))
