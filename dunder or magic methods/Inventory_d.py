class Inventory:
    def __init__(self):
        self.l=[]
    def __add__(self, other):
        self.l.append(other)
        return self.l

i1=Inventory()
print(i1+"Pencil")  # ['Pencil']


# i1.__add__("Pencil")              # Internal Process
# Inventory.__add__(i1,"Pencil")    # Internal Process