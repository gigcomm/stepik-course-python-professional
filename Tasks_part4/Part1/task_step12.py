import sys

nums = [int(line.strip()) for line in sys.stdin]
if not nums:
    print("Дима")
else:
    last_nums = nums[-1]
    last_person = "Анри" if len(nums) % 2 == 1 else "Дима"

    if last_nums % 2 == 0:
        print(last_person)
    else:
        print("Дима" if last_person == "Анри" else "Анри")