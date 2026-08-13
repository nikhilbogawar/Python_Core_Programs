class User:
    def __init__(self,n,a,g,dob):
        self.name=n
        self.age=a
        self.gender=g
        self.dob=dob

    def login(self):
        print("Login successful")

    def logout(self):
        print("Logout successful")

class Instagram(User):
    def post(self):
        print(f"{self.name} post")
        print("Got 1L likes")

i1=Instagram("Nikhil",21,"Male","15 Jan 2005")
i1.login()
i1.post()
i1.logout()
