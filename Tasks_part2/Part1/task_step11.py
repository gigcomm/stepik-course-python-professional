def index_of_nearest(numbers: list[int], number: int):
    if not numbers:
        return -1
    return min(range(len(numbers)), key=lambda i: (abs(numbers[i]-number), i))