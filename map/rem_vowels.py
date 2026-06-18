l=["Hello", 'Hii', "Who','are", "you?"]
k=[]
def fun(x):
    if x not in "AEIOUaeiou":
        return x
    return ""
for i in l:
    s=list(map(fun,i))
    s="".join(s)
    k.append(s)
print(k)           # ['Hll', 'H', "Wh','r", 'y?']
def fun2(y):
    s=0
    for i in y:
        s+=ord(i)
    return s
A=list(map(fun2,k))
print(A)           # [288, 72, 427, 184]


# Removing Vowels from a List of Strings Using map()
# l = ["Hello", "hii", " will ','you", "be"]
# def rv(word):
#     cw = ""                      
#     for char in word:                      
#         if char not in "AEIOUaeiou":       
#             cw = cw + char  
#     return cw                   
# res = list(map(rv, l))
# print(res)