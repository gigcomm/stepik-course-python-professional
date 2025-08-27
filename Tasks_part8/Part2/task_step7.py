def output_numbers(numbers):
    def rec(number):
        if number < len(numbers):
            print(f'Элемент {number}: {numbers[number]}')
            rec(number+1)
    rec(0)

output_numbers([1,2,3,4,5])