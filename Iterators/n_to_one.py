# Create an custom iterator that prints numbers from N to 1.

class NToOne:
    def __init__(self, n):
        self.current = n
    def __iter__(self):
        return self
    def __next__(self):
        if self.current >= 1:
            val = self.current
            self.current -= 1
            return val
        else:
            raise StopIteration
for num in NToOne(5):
    print(num)
