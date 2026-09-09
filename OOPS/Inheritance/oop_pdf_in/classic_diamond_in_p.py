# Create the classic diamond problem: A → B, A → C, D(B,C). Give all four classes a
# method hello() that returns their name. Show which hello() gets called on D(). Then
# remove hello() from B and show how the MRO changes the result.
class A:
    def hello(self):
        return "Hello from A"

class B(A):
    def hello(self):
        return "Hello from B"

class C(A):
    def hello(self):
        return "Hello from C"

class D(B, C):
    pass

d = D()
print(d.hello())        # Which one gets called?
print(D.__mro__)        # See resolution order

# If we remove hello() from B:
class B(A):  # no hello here
    pass

class D(B, C):
    pass

d = D()
print(d.hello())        # Now it resolves differently
print(D.__mro__)
