def zip_longest(*args, fill=None):
    max_length = max(len(arg) for arg in args) if args else 0
    return [tuple(lst[i] if i < len(lst) else fill for lst in args) for i in range(max_length)]

data = [[1, 2, 3, 4, 5], ['one', 'two', 'three'], ['I', 'II']]
print(zip_longest(*data))