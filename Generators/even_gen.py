def even(l):
    for i in l:
        if i%2==0:
            yield i

k=even([1,2,3,3,7,8,2,10])
print(next(k))
print(next(k))
for i in k:
    print(i)