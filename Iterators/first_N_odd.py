# # Create an custom iterator that prints the first N odd numbers.

class OddNumbers:
    def __init__(self, n):
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.n:
            val = 2 * self.count + 1
            self.count += 1
            return val
        else:
            raise StopIteration

for num in OddNumbers(5):
    print(num)
