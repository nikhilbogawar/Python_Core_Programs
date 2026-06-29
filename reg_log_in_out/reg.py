profiles = {}

def register():
    k = {}
    global profiles
    k["Name"] = input("Enter your Name: ")
    k["Age"] = int(input("Enter your Age: "))
    k["Email"] = input("Enter your Email: ")
    k["Phno"] = input("Enter your Phone Number: ")
    k["Pass"] = input("Enter Password: ")
    while True:
        username = input("Enter your Username: ")
        if username in profiles.keys():
            print("Username Already Exists")
            continue
        profiles[username] = k
        break   

def login():
    username = input("Enter your Username: ")
    if username in profiles:
        password = input("Enter your Password: ")
        if password == profiles[username]["Pass"]:
            print("Login Successful")
            return username
        else:
            print("Incorrect password, please try again")
            return None
    else:
        print("Username not found")
        return None

def logout(current_user):
    if current_user:
        print(f"User '{current_user}' has been logged out")
    else:
        print("No user is currently logged in")

register()
current_user = login()
logout(current_user)
