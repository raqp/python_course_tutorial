class PowTwo:
    def __init__(self, max=0):
        self.max = max
        self.n = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


a = PowTwo(3)
i = iter(a)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))