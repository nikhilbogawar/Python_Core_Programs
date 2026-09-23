class Snapchat:
    users = {}
    def __init__(self, name, username, age, gender, password):
        self.name = name
        self.username = username
        self.age = age
        self.gender = gender
        self.password = password
        self.logged = False
        self.friends = []
        self.streaks = {}
        Snapchat.users[username] = self

    @classmethod
    def signup(cls):
        name = input("Enter your Name: ")
        while True:
            username = input("Enter your Username: ")
            if username in cls.users:
                print("Username already exists, try another one")
                continue
            break
        age = input("Enter your Age: ")
        gender = input("Enter your Gender (Male/Female): ")
        password = input("Enter your Password: ")
        return cls(name, username, age, gender, password)

    def login(self):
        if self.logged:
            print("Already logged in")
        else:
            user = input("Enter your Username: ")
            password = input("Enter your Password: ")
            if user == self.username and password == self.password:
                self.logged = True
                print("Login Successful")
            else:
                print("Invalid Credentials")

    def logout(self):
        if self.logged:
            self.logged = False
            print("Logged out successfully")
        else:
            print("Already logged out")

    def add_friend(self, user):
        if self.logged:
            if user not in self.friends:
                self.friends.append(user)
                self.streaks[user.username] = 0
                print(f"{user.username} added as a friend")
            else:
                print("Already friends")
        else:
            print("Not logged in")

    def remove_friend(self, user):
        if self.logged:
            if user in self.friends:
                self.friends.remove(user)
                self.streaks.pop(user.username, None)
                print(f"{user.username} removed from friends")
            else:
                print("Friend not found")
        else:
            print("Not logged in")

    def send_snap(self, user):
        if self.logged:
            if user in self.friends:
                self.streaks[user.username] += 1
                user.streaks[self.username] += 1
                print(f"Snap sent to {user.username}! Current streak: {self.streaks[user.username]}")
            else:
                print("User is not your friend")
        else:
            print("Not logged in")

    def miss_day(self):
        for friend in self.streaks:
            self.streaks[friend] = 0
        print("Missed a day! All streaks reset.")

    def profile(self):
        print(f"{self.name}'s Profile")
        print(f"Username: {self.username}")
        print(f"Age: {self.age}")
        print(f"Gender: {self.gender}")
        print(f"Friends: {[f.username for f in self.friends]}")
        print(f"Streaks: {self.streaks}")

u1 = Snapchat.signup()
u2 = Snapchat.signup()

u1.login()
u2.login()

u1.add_friend(u2)
u2.add_friend(u1)

u1.send_snap(u2)
u2.send_snap(u1)

u1.profile()
u2.profile()

u1.miss_day()
u1.profile()
