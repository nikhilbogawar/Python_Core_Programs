l=['song1','song2','song3','song4','song5']
it=iter(l)
it2=l.__iter__()
print(it,it2,sep='\n')
print(it.__next__())
print(next(it))
print(next(it2))
print(it2.__next__())