#возможно модернезировать данный код при помщи метода ".get()", если какого-то ключа нет в словаре
import json

def is_time_in_range(work_hours, start_time='10:00', end_time='12:00'):
    open_time, close_time = work_hours.split('-')
    return open_time <= start_time and close_time >= end_time


with open('pools.json', 'r', encoding='utf-8') as file:
    pools = json.load(file)

result = []

for pool in pools:
    working_hours_summer = pool['WorkingHoursSummer']
    if is_time_in_range(working_hours_summer['Понедельник']):
        address = pool['Address']
        square = pool['DimensionsSummer']['Length']
        width = pool['DimensionsSummer']['Width']
        result.append((square, width, address))

if result:
    result.sort(key=lambda x: (-x[0], -x[1]))
    best_pool = result[0]
    print(f"{best_pool[0]}x{best_pool[1]}")
    print(best_pool[2])