d1 = int(input())
d2 = int(input())
d3 = int(input())

path1 = d1 + d2 + d3
path2 = 2 * (d1 + d3)
path3 = 2 * (d1 + d2)
path4 = 2 * (d2 + d3)

res = min(path1, path2, path3, path4)
print(res)