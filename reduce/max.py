l=[3,5,1,7,4,8,2]
from functools import reduce
k=reduce(lambda x,y:max(l),l)
print(k)