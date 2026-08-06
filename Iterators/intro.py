# Iterators: are pointers which points at each other

# l=len("7910218")
# print(l)  # 7

# s="Hello"
# for i in s:
#     print(i,end=" ")  # H e l l o

# k=(7,8,9,5,4,6,1,2)
# l=iter(k)           # used in for loop
# print(l) # prints address
# print(next(l))  # 7     # "next" used in for loop
# print(next(l))  # 8


# two iterators generate:--------
# l=[1,3,(1,2,3),"Hello"]
# it1=iter(l)
# it2=iter(l)
# print(it1,it2)  # prints address
# print(next(it1))  # 1          # for this we can call or write as it1.__next__()
# print(next(it1))  # 3
# print(next(it1))  # (1,2,3)
# print(next(it2))  # 1          # for this we can call or write as it2.__next__()

# st="Hello (Who,are)? you?"
# it=st.__iter__()
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(next(it))
# print(it.__next__())
# print(it.__next__())
# print(next(it))