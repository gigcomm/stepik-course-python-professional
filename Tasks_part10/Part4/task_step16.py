class Alphabet:
    def __init__(self, language):
        self.language = language
        self.ru = ['а', 'б', 'в', 'г', 'д', 'e']
        self.en = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.language == 'en':
            result = self.en[self.index % len(self.en)]
            self.index += 1
            return result
        elif self.language == 'ru':
            result = self.ru[self.index % len(self.ru)]
            self.index += 1
            return result

en_alpha = Alphabet('en')
letters = [next(en_alpha) for _ in range(28)]
print(*letters)
