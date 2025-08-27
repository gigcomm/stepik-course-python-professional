import sys

def rec():
    num = int(sys.stdin.readline())
    if num != 0:
        rec()
        print(num)

rec()

