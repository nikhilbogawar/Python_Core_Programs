l=[2,3,4,5,8,7,6,5,4,3,3,5,6,4,2,6]
m=sorted(l,key=lambda x:x%5)
k=sorted(l,key=lambda x:x%5, reverse=True)
print(k)
print(m)