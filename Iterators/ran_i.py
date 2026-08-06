class Ran:
    def __init__(self,start,end):
        self.start=start
        self.end=end
    def __iter__(self):
        return self
    def __next__(self):
        if self.start<=self.end:
            self.start+=1
            return self.start
        else:
            return "Invalid"
r1=Ran(3,11)
print(next(r1))
r=iter(r1)  # r=r1
print(next(r))
print(r1.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())
print(r.__next__())