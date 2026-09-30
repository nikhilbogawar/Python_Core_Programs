# • Create a class PasswordValidator with a method validate(password).
# Raise an exception if the password length is less than 8 characters.
class PasswordValidator:
    def validate(self, password):
        if len(password) < 8:
            raise Exception("Password must contain at least 8 characters")
        print("Password is valid")
p = PasswordValidator()
try:
    p.validate("nikhil")
except Exception as e:
    print("Error:", e)