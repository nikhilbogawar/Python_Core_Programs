# create a custom iterator that takes the A string and returns the cumulative sum Ascii values of the character

class CumulativeAscii:
    def __init__(self,s):
        self.s=s
        self.i=0
        self.total=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.s):
            self.total += ord(self.s[self.i-1])
            self.i+=1
            return self.total
        else:
            raise StopIteration
a1=CumulativeAscii("Nikhil")
a=iter(a1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
