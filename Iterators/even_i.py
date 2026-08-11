class EvenFromList:
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


e1=EvenFromList([1,54,61,641,5,6,43,98,42])
for i in e1:
    print(i,end=" ")


# class OddFromList:
#     def __init__(self, lst):
#         self.lst = lst
#         self.index = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         while self.index < len(self.lst):
#             val = self.lst[self.index]
#             self.index += 1
#             if val % 2 != 0:
#                 return val
#         raise StopIteration
#
#
# for num in OddFromList([1, 2, 3, 4, 5, 6]):
#     print(num)
