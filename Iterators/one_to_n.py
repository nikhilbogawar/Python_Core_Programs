# 1.	Create an custom iterator that prints numbers from 1 to N, where N is given by the user.

class OneToN:
    def __init__(self, n):
        self.n = n
        self.current = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.current <= self.n:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration

for i in OneToN(5):
    print(i)
