c = [23,22,26,10,15,20]
m = sorted(filter(lambda x: 60<x<120, map(lambda x: int(x*9/5)+32, c)), key=lambda x:x%4)
print(m)    #[68,73,78,71]