from collections import OrderedDict

def custom_sort(ordered_dict, by_values=False):
    if by_values:
        sorted_items = sorted(ordered_dict.items(), key=lambda x: x[1])
    else:
        sorted_items = sorted(ordered_dict.items(), key=lambda x: x[0])

    ordered_dict.clear()
    ordered_dict.update(sorted_items)

data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)
print(*data.items())