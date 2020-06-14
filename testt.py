class Series:

    def __init__(self, start, stop):
        self.current = start
        self.high = stop

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


custom_iterator = Series(1, 4)

for i in custom_iterator:
    print(i)
