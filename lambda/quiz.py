# Quiz question:
k=[[1,2],[4,5],[6,7]]
l=[]
m=lambda x:x.append(25)
for i in k:
    l.append(m(i))
print(k)              # [[1, 2, 25], [4, 5, 25], [6, 7, 25]]
print(l)              # [None, None, None] because append() function returns None value