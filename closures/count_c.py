# Create a function counter().
#
# -   Inside it, initialize a variable count = 0.
# -   Create an inner function that increments count by 1 every time it is
#     called and prints the updated value.
# -   Return the inner function.
# -   Call the returned function five times.
def counter():
    count=0
    def increment():
        nonlocal count
        count=count+1
        print(f"Count : {count}")
    return increment
c1=counter()
c1()
c1()