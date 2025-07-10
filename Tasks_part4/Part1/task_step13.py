import sys

heights = [int(line.strip()) for line in sys.stdin]
if not heights:
    sys.stdout.write("нет учеников")
else:
    sys.stdout.write(f"Рост самого низкого ученика: {min(heights)}\n")
    sys.stdout.write(f"Рост самого высокого ученика: {max(heights)}\n")
    sys.stdout.write(f"Средний рост: {sum(heights)/len(heights)}\n")
