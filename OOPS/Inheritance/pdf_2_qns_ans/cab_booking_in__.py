# Class 1: Cab
# Class 1: Cab
class Cab:
    def fare(self, cab_type, km):
        rates = {"Bike": 10, "Auto": 15, "Car": 20}  # per km rates
        cab_type = cab_type.strip().title()  # normalize input
        return rates.get(cab_type, 0) * km

class Uber(Cab):
    def __init__(self):
        self.bookings = []

    def menu(self):
        print("---- Uber Cab Menu ----")
        print("Bike: ₹10/km")
        print("Auto: ₹15/km")
        print("Car : ₹20/km")
        print("-----------------------")

    def booking(self):
        while True:
            cab_type = input("Enter cab type (Bike/Auto/Car) or 'done' to finish: ").strip().title()
            if cab_type.lower() == "done":
                break
            km = int(input(f"Enter distance in km for {cab_type}: "))
            self.bookings.append((cab_type, km))
            print(f"{cab_type} booked for {km} km.")

    def billing(self):
        total = sum(self.fare(cab, km) for cab, km in self.bookings)
        gst = total * 0.10
        total += gst
        if total > 1000:
            discount = total * 0.15
            total -= discount
            print(f"15% discount applied: -₹{discount:.2f}")
        print("\n---- Uber Bill ----")
        for cab, km in self.bookings:
            print(f"{cab} ({km} km): ₹{self.fare(cab, km)}")
        print(f"GST (10%): ₹{gst:.2f}")
        print(f"Total Amount: ₹{total:.2f}")
        print("-------------------")

class Ola(Cab):
    def __init__(self):
        self.bookings = []

    def menu(self):
        print("---- Ola Cab Menu ----")
        print("Bike: ₹10/km")
        print("Auto: ₹15/km")
        print("Car : ₹20/km")
        print("----------------------")

    def booking(self):
        while True:
            cab_type = input("Enter cab type (Bike/Auto/Car) or 'done' to finish: ").strip().title()
            if cab_type.lower() == "done":
                break
            km = int(input(f"Enter distance in km for {cab_type}: "))
            self.bookings.append((cab_type, km))
            print(f"{cab_type} booked for {km} km.")

    def billing(self):
        total = sum(self.fare(cab, km) for cab, km in self.bookings)
        gst = total * 0.12
        total += gst
        if total > 1500:
            discount = total * 0.20
            total -= discount
            print(f"20% discount applied: -₹{discount:.2f}")
        print("\n---- Ola Bill ----")
        for cab, km in self.bookings:
            print(f"{cab} ({km} km): ₹{self.fare(cab, km)}")
        print(f"GST (12%): ₹{gst:.2f}")
        print(f"Total Amount: ₹{total:.2f}")
        print("------------------")

choice = input("Choose Cab Service (Uber/Ola): ")

if choice.lower() == "uber":
    service = Uber()
elif choice.lower() == "ola":
    service = Ola()
else:
    print("Invalid choice!")
    exit()

service.menu()
service.booking()
service.billing()
