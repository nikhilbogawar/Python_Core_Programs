class Bank:
    Bank_name="Bank of Baroda"
    def __init__(self,name,acc_no,mb_no):
        self.name=name
        self.account_no=acc_no
        self.mobile_no=mb_no
        self.balance=0
        self.pin=int(input("Enter Pin:"))

bank1=Bank("Nikhil",741369852456,9876543210)
print(bank1.__dict__)