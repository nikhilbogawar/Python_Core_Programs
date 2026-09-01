# Q4. Create a base class Transport with move() and derived classes Bus and Bike that
# override it but also call the parent implementation using super().
# Show the combination of reuse + custom behavior.
class Transport:
    def move(self):
        print("move")
class Bus(Transport):
    def move(self):
        super().move()
        print("Bus")
class Bike(Transport):
    def move(self):
        super().move()
        print("Bike")
    