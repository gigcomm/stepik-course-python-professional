# def convert(string):
#     count = 0
#     for ch in string:
#         if ch.isupper():
#             count += 1
#     if count > len(string) // 2:
#         return string.upper()
#     else:
#         return string.lower()

def convert(string):
    upper_count = sum(1 for ch in string if ch.isupper())
    lower_count = sum(1 for ch in string if ch.islower())
    return string.upper() if upper_count > lower_count else string.lower()
print(convert('pyTHON'))

