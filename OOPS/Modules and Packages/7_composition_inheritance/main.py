# 7. Create a module containing two classes where one uses composition and another
# uses inheritance to reuse code from a base class. Import and demonstrate the
# difference between the two approaches.
from employee import Employee, Developer
e=Employee()
e.display()

d=Developer()
d.work()