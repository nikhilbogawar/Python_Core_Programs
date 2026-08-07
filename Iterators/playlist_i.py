class PlayList:
    def __init__(self,list):
        self.list=list
        self.index=0

    def __iter__(self):
        return self
    def __next__(self):
        if self.index<len(self.list):
            song=self.list[self.index]
            self.index+=1
            return song


p1= PlayList(['Hoyna Hoyna','Laka Laka Laka','Adento Gani Unnapatuga','Natu Natu'])
p2= PlayList(['Wanna Fly','Irumudi','Gusa Gusalade','Colorful Chilaka'])
p=iter(p1)
q=iter(p2)
print(next(p))
print(next(p))
print(next(p))
print(next(p))

# print(next(p))
# print(next(p))
# print(next(p))
# print(next(p))

print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))
print(next(q))


for i in p2:
    if i is None:
        break
    print(i)