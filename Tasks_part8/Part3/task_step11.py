def get_fast_pow(a, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        temp = get_fast_pow(a, n//2)
        return temp * temp
    else:
        return a * get_fast_pow(a, n-1)

print(get_fast_pow(5, 4))