# • Create a class UserInput with a method get_integer(value).
# Handle ValueError and TypeError using separate except blocks.
class UserInput:
    def get_integer(self, value):
        try:
            number = int(value)
            print("Integer:", number)
        except ValueError:
            print("Error: Invalid value. Cannot convert to integer.")
        except TypeError:
            print("Error: Type is not valid.")
u = UserInput()
u.get_integer("100")
u.get_integer("hello")
u.get_integer(None)