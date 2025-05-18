def same_parity(numbers):
    if not numbers:
        return []
    return [num for num in numbers if num % 2 == numbers[0] % 2]

print(same_parity([6, 0, 67, -7, 10, -20]))