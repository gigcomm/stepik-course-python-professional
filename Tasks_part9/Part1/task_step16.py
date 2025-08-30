def custom_sort(s):
    lowercase = sorted([ch for ch in s if ch.islower()])
    uppercase = sorted([ch for ch in s if ch.isupper()])
    odd_digits = sorted([ch for ch in s if  ch.isdigit() and int(ch) % 2 ==1])
    even_digits = sorted([ch for ch in s if ch.isdigit() and int(ch) % 2 == 0])

    return ''.join(lowercase + uppercase + odd_digits + even_digits)

s = input().strip()
print(custom_sort(s))