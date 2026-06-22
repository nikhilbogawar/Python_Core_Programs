#   Use a lambda with .sort() to sort this list of tuples by the second element: [(1,'banana'),(2,'apple'),(3,'cherry')]
l=[(1,'banana'),(2,'apple'),(3,'cherry')]
k=sorted(l,key=lambda x:x[1])
print(k)