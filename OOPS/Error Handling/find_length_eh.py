# • Write a function named find_length(obj) that uses a loop to calculate the length
# of the given object without using the built-in len() function.
# The function should return the calculated length if the object is iterable.
# If a non-iterable object such as an integer is passed,
# the function should raise and handle a TypeError,
# and print an appropriate error message explaining what happens when an integer is sent as input.
def find_length(obj):
    # if isinstance(obj,(str,list,tuple,set)):
    #     c=0
    #     for _ in obj:
    #         c+=1
    #     return c
    # elif isinstance(obj,dict):
    #     c=0
    #     for i,j in obj.items():
    #         c+=1
    #     return c
    # else:
    #     raise TypeError("object must be iterable")
    try:
        count = 0
        for item in obj:
            count += 1
        return count
    except TypeError:
        print("Error: Integer is not iterable and its length cannot be calculated.")
print(find_length("Hello"))
print(find_length([10, 20, 30, 40]))
find_length(100)