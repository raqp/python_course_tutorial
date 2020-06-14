class Iterator:

    def __init__(self, obj, start=0):
        self.obj = obj
        self.limit = len(obj)
        self.count = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        if -1 <= self.count < self.limit - 1:
            self.count += 1
            return self.obj[self.count]
        raise StopIteration

    def rnext(self):
        loc_obj = self.obj[self.count]
        self.count -= 1
        if self.count == (self.limit + 2) * -1:
            raise StopIteration
        return loc_obj


a = [1, 2, 3, 4, 5]

b = Iterator(a)

for i in b:
    print(i)
