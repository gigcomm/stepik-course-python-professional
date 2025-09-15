class DictItemsIterator:
    def __init__(self, data):
        self.data = data
        self.keys = list(data)
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        key = self.keys[self.index]
        value = self.data[key]
        self.index += 1
        return (key, value)

pairs = DictItemsIterator({1: 'A', 2: 'B', 3: 'C'})
print(*pairs)