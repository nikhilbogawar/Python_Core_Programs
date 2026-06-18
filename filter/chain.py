# chain map() and filter to the list upto 1 to 10 filter out odds and print the remaining evens and for every even element square it
l=[1,2,3,4,5,6,7,8,9,10]
k=list(filter(lambda x:x%2==0 ,l))
print(k)
m=list(map(lambda x:x**2 ,k))
print(m)