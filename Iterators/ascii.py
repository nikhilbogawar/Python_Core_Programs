# create a custom iterator that takes the A string and returns Ascii values of the character

class Ascii:
    def __init__(self,s):
        self.s=s
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.i < len(self.s):
            self.i+=1
            return ord(self.s[self.i-1])
        else:
            raise StopIteration
a1=Ascii("Nikhil")
a=iter(a1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
