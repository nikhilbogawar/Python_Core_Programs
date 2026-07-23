# total length of the inventory (should be Merge all)
class Inventory:
    def __init__(self,l):
        self.Iv=l
    def add(self, item):
        self.Iv.extend(item)      # using extend instead of append
    def __add__(self, other):
        k=self.Iv+other.Iv
        return Inventory(k)
i1=Inventory([])
i2=Inventory([])
i3=Inventory([])
i1.add(["Burger","Kinder Joy"])
i2.add(["Pasta","Noodles"])
i3.add(["Dosa","Idly"])
i4=i1+i2+i3
print(i4.Iv)   # ['Burger', 'Kinder Joy', 'pasta', 'momos', 'dosa', 'idly']