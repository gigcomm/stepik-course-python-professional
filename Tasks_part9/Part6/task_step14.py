def get_digits(number: int | float) -> list[int]:
    return [int(num) for num in str(number) if num.isdigit()]

print(get_digits(7679.645))