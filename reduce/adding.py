l=[1,3,2,5,6,3]
from functools import reduce
k=reduce(lambda x,y:x+y,[],20)
m=reduce(lambda x,y:x+y,l,20)
print(k)
print(m)

# l=[5,10,15,20,25,30]
# from functools import reduce
# k=reduce(lambda x,y:x+y,l)
# print(k)