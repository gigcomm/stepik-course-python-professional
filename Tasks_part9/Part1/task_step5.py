def convert(number):
    return (bin(number).split('0b')[-1], oct(number).split('0o')[-1], hex(number).split('0x')[-1])

print(convert(15))