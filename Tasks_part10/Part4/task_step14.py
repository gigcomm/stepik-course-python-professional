from operator import index


class Cycle:
    def __init__(self, iterable):
        self.iterable = iterable
        self.elements = list(iterable)
        self.index = 0
        self.length = len(self.elements)

    def __iter__(self):
        return self

    def __next__(self):
        if self.length == 0:
            raise StopIteration

        result = self.elements[self.index]
        self.index = (self.index + 1) % self.length
        return result



cycle = Cycle('be')
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))