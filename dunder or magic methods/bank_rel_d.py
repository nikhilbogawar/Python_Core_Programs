class Bank:
    def __init__(self,Name,acc):
        self.Name=Name
        self.acc=acc
        self.bal=0
    def __hash__(self):
        return hash(self.acc)
b1=Bank("Nikhil",1543)
b2=Bank("Nikhil",1875)
k={b1,b2}
print(k)  # {<__main__.Bank object at 0x000001E9099C8410>, <__main__.Bank object at 0x000001E9099D4590>}