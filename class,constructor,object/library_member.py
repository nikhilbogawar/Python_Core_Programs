# Design a LibraryMember class that:
# •	Tracks total active members.
# •	Each member has a name and books_borrowed count.
# •	Has a function to borrow books, with borrowing limit common to all.
# •	Allows updating borrowing limit globally.
# •	Has a static function to check if book title is valid (non-empty string, reasonable length).
# Demonstrate:
# 1.	Borrowing books for multiple users.
# 2.	Changing borrowing limits.
# 3.	Validating book titles before borrowing.

class LibraryMember:
    total_members=0
    borrow_limit=3
    def __init__(self,name):
        self.name=name
        self.books_borrowed=0
        LibraryMember.total_members+=1

    def borrow_book(self,title):
        if self.books_borrowed < LibraryMember.borrow_limit and LibraryMember.is_valid_title(title):
            self.books_borrowed=+1
            print(self.name, "borrowed", title)
        else:
            print("cannot borrow")

    @classmethod
    def update_limit(cls,new_limit):
        cls.borrow_limit=new_limit

    @staticmethod
    def is_valid_title(title):
        return isinstance(title,str) and len(title)>=3

m1=LibraryMember("Nikhil")
m1.borrow_book("Python")
m1.borrow_book("Java")
LibraryMember.update_limit(5)
m1.borrow_book("DSA")
