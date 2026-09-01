# Q2. Write a function operate(device) that calls device.start().
# Pass in objects of Car, Computer, and WashingMachine — all of which define a start()
# method, but share no inheritance relationship.
# Show that Python’s polymorphism works through behavior, not type.
def operate(device):
    device.start()
class Car:
    def start(self):
        print("starting the car")
class Computer:
    def start(self):
        print("turn on")
class WashingMachine:
    def start(self):
        print("washing")
k=[Car(),Computer(),WashingMachine()]
for i in k:
    operate(i)