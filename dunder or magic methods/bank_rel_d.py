class Bank:
    def __init__(self,Name,acc):
        self.Name=Name
        self.acc=acc
        self.bal=0
    def __hash__(self):
        return hash(self.acc)
    def __str__(self):
        return f"Name: {self.Name}, Account: {self.acc}, Balance: {self.bal}"
    def __repr__(self):
        return self.__str__()
b1=Bank("Nikhil",1543)
b2=Bank("Nikhil",1875)
k={b1,b2}
print(k)  # {Name: Nikhil, Account: 1875, Balance: 0, Name: Nikhil, Account: 1543, Balance: 0}