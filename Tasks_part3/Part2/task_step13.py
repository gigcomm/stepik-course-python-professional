from datetime import date

n = int(input())

dates = [date.fromisoformat(input()) for _ in range(n)]
for d in sorted(dates):
    print(d.strftime('%d/%m/%Y'))