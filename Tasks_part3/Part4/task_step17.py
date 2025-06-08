from datetime import datetime, timedelta

t = input()
n = int(input())
try:
    time_obj = datetime.strptime(t, '%H:%M:%S')
    result_time = (time_obj + timedelta(seconds=n)).time()
    print(result_time.strftime('%H:%M:%S'))
except ValueError:
    print("Ошибка: неверный формат времени. Используйте HH:MM:SS")