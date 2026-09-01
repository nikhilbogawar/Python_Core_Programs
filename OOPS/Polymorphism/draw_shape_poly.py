# Q9. Create a function draw(shape) that works for objects of classes Circle, Square, and
# Rectangle,
# each implementing a draw() method.
# Add another unrelated class Car with draw() and pass it — what happens and why?
# Answer:-->>> Nothing happens here
def draw(shape):
    shape.draw()
class Shapes:
    pass
class Circle(Shapes):
    def draw(self):
        print("Circle")
class Square(Shapes):
    def draw(self):
        print("Square")
class Rectangle(Shapes):
    def draw(self):
        print("Rectangle")
class Car:
    def draw(self):
        print("Car")
l=[Circle(),Square(),Rectangle(),Car()]
for i in l:
    draw(i)