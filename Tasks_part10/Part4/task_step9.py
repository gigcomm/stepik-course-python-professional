class Square:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        self.count += 1
        return self.count ** 2

squares = Square(10)
print(list(squares))