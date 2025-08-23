from collections import Counter


def print_bar_chart(data, mark):
    if isinstance(data, str):
        counter = Counter(data)
    else:
        counter = Counter(data)

    max_len = max(len(str(key)) for key in counter)
    order = {key: i for i, key in enumerate(counter.keys())}
    sorted_items = sorted(counter.items(), key=lambda x: (-x[1], order[x[0]]))

    for key, count in sorted_items:
        print(f"{str(key).ljust(max_len)} |{mark * count}")


languages = ['java', 'java', 'python', 'C++', 'assembler', 'java', 'C++', 'C',
'pascal', 'C++', 'pascal', 'java']
print_bar_chart(languages, '#')