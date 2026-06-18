l=[1,2,3,5,6]
from functools import reduce
k=reduce(lambda x,y:x*y,l)
print(k)