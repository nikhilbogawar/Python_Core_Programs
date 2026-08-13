class User:
    def __init__(self,n,a,g,dob):
        self.name=n
        self.age=a
        self.gender=g
        self.dob=dob

    def login(self):
        print("Login successful")

    def logout(self):
        print("Logout successful")

class Bank(User):
    Name="SBI"
    def guidelines(self):
        print("Beware of Scammer an call 999")

class PhonePe(Bank):
    def payments(self,amount):
        print(f"{amount}rs has be paid through UPI")

u1=PhonePe("Nikhil",21,"Male","15 Jan 2005")
u2=Bank("Arjun",21,"Male","23 July 2005")
u1.login()
u1.logout()
u1.guidelines()
u1.payments(50)
print(PhonePe.mro())
# u2.login()
# u2.logout()
# u2.guidelines()
# u2.payments(60)