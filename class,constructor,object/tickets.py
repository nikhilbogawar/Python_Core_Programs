class Ticket:
    total=0
    source="Hyderabad"
    destination="Goa"
    def __init__(self,name,age,email,phone):
        self.name=name
        self.age=age
        self.email=email
        self.phone=phone
        Ticket.total+=1  # self.total+=1        we can write like this also but for this it counts in teh dictionary

ticket1=Ticket("Nikhil",21,"tejasnikhil72@gmail.com",9381383166)
ticket2=Ticket("Praveen",21,"praveen@gmail.com",9876543210)
print("Total Tickets:",Ticket.total)
print(ticket1.name)
print(ticket2.name)
print(Ticket.__dict__) # {'__module__': '__main__', '__firstlineno__': 1, 'total': 2, 'source': 'Hyderabad', 'destination': 'Goa', '__init__': <function Ticket.__init__ at 0x000001D6851B7270>, '__static_attributes__': ('age', 'email', 'name', 'phone'), '__dict__': <attribute '__dict__' of 'Ticket' objects>, '__weakref__': <attribute '__weakref__' of 'Ticket' objects>, '__doc__': None}
print(ticket1.__dict__)    # {'name': 'Nikhil', 'age': 21, 'email': 'tejasnikhil72@gmail.com', 'phone': 9381383166}
print(ticket2.__dict__)
print(ticket1.source) #Hyderabad
print(Ticket.destination)   # Goa