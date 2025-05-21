n = int(input())

numbers = list(range(1, n+1))

res_dict = {}

for num in numbers:
    digit = sum(map(int, str(num)))
    if digit not in res_dict:
        res_dict[digit] = [num]
    else:
        res_dict[digit].append(num)

max_len = max(len(num) for num in res_dict.values())
print(max_len)

