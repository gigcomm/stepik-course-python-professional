import calendar

try:
    num_date = int(input().strip())

    months = calendar.month_name
    try:
        result = months[num_date]
    except IndexError:
        print('Введено число из недопустимого диапазона')
    else:
        print(result)
except ValueError:
    print('Введено некорректное значение')

