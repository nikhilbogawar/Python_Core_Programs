class Bank:
    def __init__(self,name,account):
        self.name=name
        self.account=account
        self.balance=0
    def __str__(self):
        p=input("Enter pin:")
        if p=="123":
            return f"name:{self.name}\naccount:{self.account}\nbalance:{self.balance}"
        else:
            return "Invalid Pin"
b1=Bank("Nikhil",987438)
print(b1)