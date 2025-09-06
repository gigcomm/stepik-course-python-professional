def power(degree):
    def inner(x):
        return x**degree
    return inner

square = power(2)
print(square(5))
