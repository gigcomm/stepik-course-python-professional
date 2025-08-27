def sander_watch():
    def rec(num):
        if num == 1:
            print('1' * 16)
            rec(num + 1)
            print('1' * 16)
        elif num == 2:
            print(' ' * 2 + '2' * 12)
            rec(num + 1)
            print(' ' * 2 + '2' * 12)
        elif num == 3:
            print(' ' * 4 + '3' * 8)
            rec(num + 1)
            print(' ' * 4 + '3' * 8)
        elif num == 4:
            print(' ' * 6 + '4' * 4)
            rec(num + 1)
    rec(1)


sander_watch()
