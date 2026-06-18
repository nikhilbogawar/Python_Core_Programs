nums=[1,2,3,4]
from functools import reduce
k=reduce(lambda x,y:x+y,nums,10)
print(k)