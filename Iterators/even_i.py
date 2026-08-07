class Even:
    def __init__(self,l):
        self.l=l
        self.index=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.index<len(self.l):
            n= self.l[self.index]
            self.index+=1
            if n%2==0:
                return n
            # else:
            #     return next(self)      # Used in recursions
        else:
            raise StopIteration


e1=Even([1,54,61,641,5,6,43,98,42])
for i in e1:
    print(i,end=" ")