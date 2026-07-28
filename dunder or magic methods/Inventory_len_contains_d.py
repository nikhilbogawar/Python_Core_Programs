class Inventory:
    def __init__(self):
        self.l=[]
    def __add__(self, other):
        self.l.append(other)
        return self
    def __len__(self):
        return len(self.l)
    def __contains__(self, other):
        return other in self.l
i1=Inventory()
i1+"laptop"+"Chair"+"Sofa"
print(len(i1))  # 3
print("Chair" in i1)  # True