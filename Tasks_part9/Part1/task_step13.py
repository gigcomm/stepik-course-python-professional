def my_pow(number):
    return sum(pow(int(digit), i) for i, digit in enumerate(str(number), 1))

print(my_pow(139))