# Write a function create_password(password).
#
# -   The outer function stores the original password.
# -   The inner function receives another password.
# -   If both passwords are the same, print Access Granted; otherwise
#     print Access Denied.
# -   Return the inner function.
def create_password(org_password):
    def check_password(input_password):
        if org_password==input_password:
            return "Access Granted"
        else:
            return "Access Denied"
    return check_password
p1=create_password("Nikhil")
print(p1("Nikhil"))