# protected and private are the process which we do in encapsulation
# example on protected and private combination

class A:
    def __init__(self):
        self._x=5
        self.__y=10
    def getx(self):
        if input()=="1234":
            return self._x
        return None
    def setx(self, value):
        if value >27:
            self._x=value
        else:
            print("value of x should be greater than 27")
    @property
    def __ac(self):
        return self._x
    @__ac.setter
    def fs(self, value):
        self._x=value
    def gety(self):
        return self.__y
    def sety(self, value):
        self.__y=value
obj=A()

obj.fs=10
print(obj.getx())
# print(obj._x)
# print(obj._A__y)#name mangling
# print(obj.getx())
# print(obj.gety())
# obj.setx(100)
# print(obj.getx())



# class BankAccount:
#     def __init__(self,name):
#         self.name=name
#         self._balance=0
#         self.__atmpin="1234"
#     def getbalance(self):
#         return self._balance
#     def setpin(self,pin):
#         if input("enter previous atm pin: ")==self.__atmpin:
#             self.__atmpin=pin
#         else:
#             print("pin incorrect")
# class UPI(BankAccount):
#     def sendmoney(self,amount):
#         if self._balance>amount:
#             self._balance=self._balance-amount
#         else:
#             print("insufficient balance")
#     def receivemoney(self,amount):
#         self._balance=self._balance+amount
# b1=BankAccount("nikhil")
# print(b1.getbalance())
# upi=UPI("nikhil")
# print(upi.getbalance())
# upi.sendmoney(100)
# upi.receivemoney(1000000000000)
# upi.sendmoney(100)
# print(upi.getbalance())
#
# b1.setpin("12345")
# b1.setpin("3456")