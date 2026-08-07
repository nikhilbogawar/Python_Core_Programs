class Attendance:
    def __init__(self,students):
        self.students=students
        self.roll_no=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.roll_no<len(self.students):
            name=self.students[self.roll_no]
            self.roll_no+=1
            return name
        else:
            raise StopIteration

st1 = Attendance(["Nikhil","Nikhi","Nikh","Nik","Ni","N"])
st2 = Attendance(["Arjun","Arju","Arj","Ar","A"])
st3 = Attendance(["Rajashekar","Rajasheka","Rajashek","Rajashe","Rajash","Rajas","Raja","Raj","Ra","R"])
for i in st1:
    print(f"{i} : Present")
for i in st2:
    print(f"{i} : Present")
for i in st3:
    print(f"{i} : Present")