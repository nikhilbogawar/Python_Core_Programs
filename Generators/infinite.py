def infinite():
    x=0
    while True:
        yield x
        x+=1
l=infinite()
k=infinite()
print(next(l))
print(next(l))
print("for loop")
for i in l:
    if i>10:
        break
    print(i)
for i in k:
    print(i)
    if i>5:
        break