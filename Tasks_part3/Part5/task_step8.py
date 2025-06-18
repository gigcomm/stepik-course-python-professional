from datetime import datetime

from Tasks_part2.Part1.task_step13 import choose_plural

date_today_str = input()
date_today = datetime.strptime(date_today_str, "%d.%m.%Y %H:%M")

start_course = datetime(2022, 11, 8, 12)

if date_today > start_course:
    print("Курс уже вышел!")


delta = start_course - date_today
total_minutes = delta.total_seconds() // 60
days = delta.days
hours = int((total_minutes - days * 1440) // 60)
minutes = int(total_minutes % 60)

message = "До выхода курса осталось: "
parts = []
if days > 0:
    day_forms = ('день', 'дня', 'дней')
    parts.append(choose_plural(days, day_forms))
if hours > 0 and days > 0:
    hour_forms = ('час','часа','часов')
    parts.append(choose_plural(hours, hour_forms))
elif hours > 0:
    hour_forms = ('час', 'часа', 'часов')
    parts.append(choose_plural(hours, hour_forms))
    if minutes > 0:
        minutes_forms = ('минута','минуты','минут')
        parts.append(choose_plural(minutes, minutes_forms))
elif minutes > 0 and days == 0:
    minutes_forms = ('минута', 'минуты', 'минут')
    parts.append(choose_plural(minutes, minutes_forms))

if not parts:
    print("Курс уже вышел!")
else:
    print(message + " и ".join(parts))

