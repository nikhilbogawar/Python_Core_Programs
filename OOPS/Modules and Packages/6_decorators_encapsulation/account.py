class Account:
    def __init__(self,balance):
        self.__balance=balance
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self,amount):
        if amount>=0:
            self.__balance=amount