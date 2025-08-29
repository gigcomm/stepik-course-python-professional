def non_negative_even(numbers):
    return all(number >= 0 and number % 2 == 0 for number in numbers)


print(non_negative_even([0, 2, 4, 8, 16]))