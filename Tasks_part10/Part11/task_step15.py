from itertools import groupby


def ranges(numbers):
    result = []
    for _, group in groupby(enumerate(numbers), key=lambda x: x[1]-x[0]):
        group_list = list(group)
        result.append((group_list[0][1], group_list[-1][1]))
    return result



numbers = [1, 2, 3, 4, 7, 8, 10]
print(ranges(numbers))

numbers = [1, 3, 5, 7]
print(ranges(numbers))

numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))
