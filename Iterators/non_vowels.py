# create a custom iterator that takes that the A while sentence and returns non_vowels only

class Sen:
    def __init__(self,s):
        self.s=s
        self.i=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.i < len(self.s):
            self.i+=1
            if self.s[self.i-1] not in "aeiouAEIOU":
                return self.s[self.i-1]
        raise StopIteration
s1=Sen("Nikhil")
c=iter(s1)
print(next(c))
print(next(c))
print(next(c))
print(next(c))