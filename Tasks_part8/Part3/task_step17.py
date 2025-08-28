def no_for(n):
    print(n)
    if n > 0:
        no_for(n - 5)
        print(n)



n = int(input())
no_for(n)