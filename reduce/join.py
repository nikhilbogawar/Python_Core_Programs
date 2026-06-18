l=['p','y','t','h','o','n']
from functools import reduce
k=reduce(lambda x,y:''.join(l),l)
print(k)