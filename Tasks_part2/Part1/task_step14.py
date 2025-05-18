def get_biggest(numbers):
    sorted_nums = sorted(map(str, numbers), key=lambda x: x*10, reverse=True)
    return sorted_nums

print(get_biggest([61, 228, 9, 3, 11]))