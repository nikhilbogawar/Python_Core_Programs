# Create an custom iterator that prints each character of a string one by one.

class StringIterator:
    def __init__(self, s):
        self.s = s
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.s):
            val = self.s[self.index]
            self.index += 1
            return val
        else:
            raise StopIteration

for ch in StringIterator("Nikhil"):
    print(ch)

# Create an custom iterator that prints the characters of a string in reverse order.

class ReverseStringIterator:
    def __init__(self, s):
        self.s = s
        self.index = len(s) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= 0:
            val = self.s[self.index]
            self.index -= 1
            return val
        else:
            raise StopIteration

for ch in ReverseStringIterator("Nikhil"):
    print(ch)
