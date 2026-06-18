# from functools import reduce
# k=[1,2,3,4,5,6,7,8,9,10]
# m=list(map(lambda x:x*7, filter(lambda x: x%3==0,k)))
# l=reduce(lambda x,y:x+y,m)
# print(l)     #126
# or
# Pipelines:---------------->>>
from functools import reduce
k=[1,2,3,4,5,6,7,8,9,10]
m=reduce(lambda x,y:x+y, filter(lambda x:x%3==0, map(lambda x:x*7,k)))
print(m)    #126