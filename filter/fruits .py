d={"apple": 100, "Banana": 40, "cherry": 150}
k=list(filter(lambda x:d[x]>50,d))
m=list(filter(lambda x:x>50,d.values()))
print(k)      # ['apple', 'cherry']
print(m)      # [100, 150]