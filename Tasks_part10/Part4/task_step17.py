class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.first_call = True

    def __iter__(self):
        self.first_call = True
        return self

    def __next__(self):
        if self.first_call:
            self.first_call = False
            current = self.start
        else:
            current = self.start + self.step
            self.start = current

        if (self.step > 0 and current >= self.end) or (self.step < 0 and current <= self.end):
            raise StopIteration

        return current

xrange = Xrange(0, 3, 0.5)
print(*xrange, sep='; ')



evens = Xrange(0, 10, 2)
print(*evens)

