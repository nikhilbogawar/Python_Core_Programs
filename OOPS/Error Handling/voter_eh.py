# • Create a custom exception named InvalidAgeError.
# Create a class Voter with a method check_eligibility(age) that raises this exception if age is less than 18.
class InvalidAgeError(Exception):
    pass
class Voter:
    def check_eligibility(self, age):
        if age < 18:
            raise InvalidAgeError("You are not eligible to vote")
        print("You are eligible to vote")
v = Voter()
try:
    v.check_eligibility(16)
except InvalidAgeError as e:
    print("Error:", e)