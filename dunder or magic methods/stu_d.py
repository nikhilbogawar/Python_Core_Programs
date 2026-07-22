class Student:
    total_students=0
    def __init__(self,name,age,clas,sec):
        self.name=name
        self.age=age
        self.sec=sec
        self.clas=clas
        Student.total_students=+1
    def __str__(self):
        return f"name:{self.name}\nage:{self.age}\nclass:{self.clas}\nsection:{self.sec}\ntotal-students:{self.total_students}"
    def __repr__(self):
        return self.name
s1=Student("Nikhil",21,10,"A")
s2=Student("Arjun",21,9,"B")
print(s1)
print(s2)
l=[s1,s2]
print(l)
# Output:-->
# name:Nikhil
# age:21
# class:10
# section:A
# total-students:1
# name:Arjun
# age:21
# class:9
# section:B
# total-students:1
# [Nikhil, Arjun]