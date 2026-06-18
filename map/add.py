a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
k=list(map(lambda x,y:x+y,a,b))
print(k)

# another example in map functions:
# l1=[1,2,3,4,5]
# l2=[10,11,12,13,14]
# l3=[25,26,27,28,29]
# k=list(map(lambda x,y,z:x+y+z,l1,l2,l3))
# print(k)   # [36, 39, 42, 45, 48]