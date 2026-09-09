# Build a multiple inheritance scenario: class Printable with a method print_info(),
# class Saveable with save(). Create class Document(Printable, Saveable) that uses
# both. Print the MRO and explain the resolution order.
class Printable:
    def print_info(self):
        return "Printable feature"

class Saveable:
    def save(self):
        return "Saveable feature"

class Document(Printable, Saveable):
    pass

doc = Document()
print(doc.print_info())
print(doc.save())
print(Document.__mro__)  # Shows Method Resolution Order
