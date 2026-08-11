# Create an custom iterator that returns only positive numbers from a list.

class PositiveFromList:
    def __init__(self, lst):
        self.lst = lst
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.lst):
            val = self.lst[self.index]
            self.index += 1
            if val > 0:
                return val
        raise StopIteration

for num in PositiveFromList([-3, -1, 0, 2, 5, -7]):
    print(num)
