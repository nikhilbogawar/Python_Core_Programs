class Cart:
    def __init__(self):
        self.l=[]
    def __add__(self, item):
        if item not in self.l:
            self.l.append(item)
        return self
    def __sub__(self, item):
        if item in self.l:
            self.l.remove(item)
        return self
    def __str__(self):
        return f"Cart Items: {self.l}"
c1=Cart()
c1+"Chips"+"Milkshake"+"ThumpsUp"+"Amul Butter"
c1-"Laptop"-"Chips"-"Mobile"
print(c1)