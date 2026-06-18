# findng consonants
k=input()
for i in k:
    if (lambda x:x not in "AEIOUaeiou")(i):
        print(i)                                 # m chstnnv