def filter_names(names, ignore_char, max_names):
    count = 0
    for name in names:
        if count >= max_names:
            break
        if name[0].lower() != ignore_char.lower() and name.isalpha():
            yield name
            count += 1


data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 'D', 3))
data = ['Dima', 'Timur', 'Arthur', 'Anri20', 'Arina', 'German', 'Ruslan']
print(*filter_names(data, 't', 20))