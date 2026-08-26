# 5. Movie Ticket Booking System Using Multilevel Inheritance
# Class 1: Movie
# • Create a method ticket(movie) that returns the ticket price.
# Class 2: Booking (inherits Movie)
# Create the following methods:
# • movies() – Display the available movies.
# • selection() – Allow the user to book multiple tickets.
# • billing() – Display the total amount and add a booking charge of ₹30.
# Class 3: Customer (inherits Booking)
# • Create an object and call the selection() method.
class Movie:
    movies_list={"Jersey":200,"Hi Nanna":180,"Hit 3":250,"Saripodha Sanivaram":220}
    def method_ticket(self,tickets):
        return self.movies_list.get(tickets,None)
class Booking(Movie):
    def __init__(self):
        self.book_tickets=[]
    def movies(self):
        print("--------Movies List---------")
        for tickets,price in self.movies_list.items():
            print(f"{tickets} : {price}rs")
        print("----------------------------")
    def selection(self):
        while True:
            movie = input("Enter Movie Name (or 'done' to finish): ")
            if movie.lower() == "done":
                break
            price = self.method_ticket(movie)
            if price is not None:
                qty = input(f"How many tickets for {movie}? ")
                if qty.isdigit() and int(qty) > 0:
                    qty = int(qty)
                    self.book_tickets.append((movie, qty))
                    print(f"{qty} tickets for {movie} added.")
                else:
                    print("Please enter a valid positive number.")
            else:
                print("Movie not available..! Please choose another movie from list")
    def billing(self):
        total = sum(self.method_ticket(movie) * qty for movie, qty in self.book_tickets)
        booking_charge = 30
        total += booking_charge
        print("----------Bill----------")
        for movie, qty in self.book_tickets:
            print(f"{movie} x {qty}: {self.method_ticket(movie) * qty}rs")
        print(f"Booking Charge: {booking_charge}rs")
        print(f"Total Amount: {total}rs")
        print("------------------------")
class Customer(Booking):
    def __init__(self,name):
        super().__init__()
        self.name=name
t1=Customer("Nikhil")
t1.movies()
t1.selection()
t1.billing()