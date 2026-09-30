# • Create a class LoginSystem with a method login(password) that
# raises an exception for an incorrect password and handles the exception outside the class
class LoginSystem:
    def login(self, password):
        if password != "12345":
            raise Exception("Incorrect password")
        print("Login successful")
login_system = LoginSystem()
try:
    login_system.login("abc")
except Exception as e:
    print("Error:", e)