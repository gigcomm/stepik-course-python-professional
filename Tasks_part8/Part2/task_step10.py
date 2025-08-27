def triagle(h):
    if h > 0:
        triagle(h - 1)
        print(h * '*')

triagle(5)
