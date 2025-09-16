def primes(left, right):
    for n in range(left, right+1):
        if n < 2:
            continue
        is_prime = True
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            yield n


generator = primes(1, 15)
print(*generator)