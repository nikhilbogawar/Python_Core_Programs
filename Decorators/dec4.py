# login by using username and password if invalid credentials print invalid or secure file

def login(func):
    def inner():
        username=input("Enter your Username:")
        password=input("Enter your Password")
        if username=="Nikhil" and password=="Nikki":
            return func()
        else:
            return "Invalid Credentials"
    return inner
@login
def secure_file():
    return "Secret File"
print(secure_file())