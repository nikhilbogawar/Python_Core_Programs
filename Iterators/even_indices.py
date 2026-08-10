class EvenIndexIterator:
    def __init__(self, l: str):
        self.l = l
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.l):
            n = self.l[self.index]
            self.index += 2
            return n
        else:
            raise StopIteration

my_string = "NikhilTejas"
iterator = EvenIndexIterator(my_string)
for char in iterator:
    print(char, end=" ")
