# if we use for __eq__ then we should use __hash__ compulsory
class Emp:
    def __init__(self, id, n):
        self.Id=id
        self.Name=n
    def __eq__(self, other):
        return self.Id==other.Id and self.Name==other.Name
    def __ne__(self, other):
        return self.Id!=other.Id and self.Name!=other.Name
    def __hash__(self):
        return hash(self.Id)
    def __str__(self):
        return f"Id: {self.Id}, Name: {self.Name}"
    def __repr__(self):
        return self.__str__()
e1=Emp(15,"Nikhil")
e2=Emp(15,"Nikhil")
print(e1==e2)  # True
print(e1!=e2)  # False
s={e1,e2}
print(s)  # {Id: 15, Name: Nikhil}