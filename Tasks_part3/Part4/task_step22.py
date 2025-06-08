from datetime import datetime, timedelta

start_work = input()
end_work = input()
start_time = datetime.strptime(start_work, "%H:%M")
end_time = datetime.strptime(end_work, "%H:%M")

lesson_time = timedelta(minutes=45)
break_time = timedelta(minutes=10)

while start_time + lesson_time <= end_time:
    lesson_start = start_time
    lesson_end = lesson_start + lesson_time
    print(f"{lesson_start.strftime("%H:%M")} - {lesson_end.strftime("%H:%M")}")
    start_time = lesson_end + break_time