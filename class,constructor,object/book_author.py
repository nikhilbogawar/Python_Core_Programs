# Create a class Book with:
# •	instance attributes title, author
# •	a class variable total_books
# •	a class method from_string(cls, book_str) that creates an object from "title-author" format
# •	a static method is_valid_title(title) that checks if title has at least 3 characters
# •	increment total_books for every book created
# Demonstrate:
# •	Creating books using both the constructor and the class method
# •	Validating titles before creation

class Book:
    total_books=0
    def __init__(self,title,author):
        self.title=title
        self.author=author
        Book.total_books=+1

    @classmethod
    def from_string(cls,book_str):
        title,author=book_str.split("-")
        if cls.is_valid_title(title):
            b=Book(title,author)
            return b
        else:
            return "Invalid Title"

    @staticmethod
    def is_valid_title(title):
        return len(title)>3

b1=Book("Bhagvatgeeta", "shri krishna")
b2=Book.from_string("Bhagvatgeeta-shri krishna")
print(b2.__dict__)  # {'title': 'Bhagvatgeeta', 'author': 'shri krishna'}


