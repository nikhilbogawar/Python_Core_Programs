profiles = {}

def register():
    k = {}
    global profiles
    k["Name"] = input("Enter your Name: ")
    k["Age"] = int(input("Enter your Age: "))
    k["Email"] = input("Enter your Email: ")
    k["Phno"] = input("Enter your Phone Number: ")
    k["Password"] = input("Enter Password: ")
    while True:
        username = input("Enter your Username: ")
        if username in profiles.keys():
            print("Username Already Exists")
            continue
        profiles[username] = k
        break   

def login():
    username = input("Enter your Username: ")
    global profiles
    if username in profiles:
        password = input("Enter your Password: ")
        if password == profiles[username]["Password"]:
            profiles[username]["logged"]=True
            print("Login Successful")
        else:
            print("Incorrect password, please try again")
    else:
        print("Username not found")

def logout(username):
    global profiles
    if username in profiles and profiles[username]["logged"]:
        profiles[username]["logged"] = False
        print("User logged out successfully")
    else:
        print("No active session for this user")


register()
current_user = login()
if current_user:
    logout(current_user)

