from datetime import date


def is_correct(day, month, year):
    try:
        date(year, month, day)
        return True
    except ValueError:
        return False

count = 0

while True:
    s = input()
    if s == "end":
        break
    try:
        day, month, year = map(int, input().split('.'))
        if is_correct(day, month, year):
            count += 1
            print("Корректная")
        else:
            print("Некорректная")
    except ValueError:
        print("Некорректная")

print(count)