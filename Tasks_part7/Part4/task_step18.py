
def get_weekday(number):
    days_ru = ["понедельник", "вторник", "среда", "четверг",
               "пятница", "суббота", "воскресенье"]
    if not isinstance(number, int):
        raise TypeError('Аргумент не является целым числом')
    if not 0 <= number <= 7:
        raise ValueError('Аргумент не принадлежит требуемому диапазону')

    return days_ru[number - 1]




try:
    print(get_weekday(8))
except ValueError as err:
    print(err)
    print(type(err))
