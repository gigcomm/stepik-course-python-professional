from itertools import combinations, permutations

s = input()
if len(s) > 10:
    input()

comb = sorted(set(permutations(s, len(s))))
for i in comb:
    print(''.join(i))
