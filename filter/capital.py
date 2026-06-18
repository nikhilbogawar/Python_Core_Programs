l=["Hello","elephant","Lion","lesson","Owl"]
k=list(filter(lambda x: bool(x) and x[0].isupper(),l))
m=list(filter(lambda y: bool(y) and y[0].islower(),l))
print(k)       # ['Hello', 'Lion', 'Owl']
print(m)       # ['elephant', 'lesson']