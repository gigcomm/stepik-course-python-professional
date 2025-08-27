def output_nature_num():
    def rec(start):
        if start <= 100:
            print(start)
            rec(start + 1)
    rec(1)

output_nature_num()