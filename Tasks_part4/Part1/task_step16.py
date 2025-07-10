import sys

lines = [line.strip() for line in sys.stdin if line.strip()]
category = lines[-1]
news_items = lines[:-1]

filtered_news = []
for item in news_items:
    parts = item.split(' / ')
    if len(parts) == 3 and parts[1] == category:
        news, cat, reliability = parts
        filtered_news.append((float(reliability), news))

filtered_news.sort(key=lambda x: (x[0], x[1]))
for reliability, news in filtered_news:
    print(news)

# На рейсах Поражения второй пилот будет исполнять обязанности бортпроводника / Авиация / 0.3
# Огурец исключит из своих рядов членов, не проголосовавших за Единую Арстоцку на выборах / Политика / 0.8
# Орбистанские точки общепита будут закрыты для вакцинированных граждан / Общество / 0.7
# Джорджи Костава получил членский билет Независимого Кобрастана / Политика / 0.0
# В Колечии повысят призывной возраст до 40 лет / Политика / 1.0
# Всем гражданам Антегрии въезд в Арстоцку запрещен / Политика / 0.8
# Политика