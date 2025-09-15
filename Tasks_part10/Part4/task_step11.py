
class PowerOf:
    def __init__(self, number):
        self.number = number + number % 2
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number < 0:
            raise StopIteration
        result = self.number ** self.count
        self.count += 1
        return result



power_of_two = PowerOf(2)
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))
print(next(power_of_two))