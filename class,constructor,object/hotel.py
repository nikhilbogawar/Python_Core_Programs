# Create a HotelRoom class that:
# •	Keeps a base price per night (shared).
# •	Each room has room_number, nights_booked, and guest_name.
# •	Has a method to calculate total bill.
# •	Allows updating the base price across all rooms.
# •	Provides a static utility to check if a number of nights is valid (e.g., positive integer only).
# Demonstrate:
# 1.	Creating rooms and bookings.
# 2.	Changing base price.
# 3.	Checking bill updates and validation.

class HotelRoom:
    base_price=1000
    def __init__(self,room_numer,nights_booked,guest_name):
        self.room_number=room_numer
        self.nights_booked=nights_booked
        self.guest_name=guest_name

    def total_bill(self):
        return self.nights_booked*HotelRoom.base_price

    @classmethod
    def update_price(cls,new_price):
        cls.base_price=new_price

    @staticmethod
    def is_valid_nights(nights):
        return isinstance(nights,int) and nights>0

room1=HotelRoom(99,4,"Nikhil")
print(room1.guest_name, room1.total_bill())

HotelRoom.update_price(1500)
print(room1.guest_name, room1.total_bill())