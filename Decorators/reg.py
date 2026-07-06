def valid(func):
    uns=[]
    special_chr=["!","@","#","$","^","%","&","*"]
    def inner(us:str,psd:str,age:int):
        nonlocal uns
        if us not in uns:
            uns.append(us)
            if 8<=len(psd)<=15:
                k=list(filter(lambda x:x in special_chr,psd))
                l=list(filter(lambda x:x.isdigit(),psd))           # l=psd.isalnum()
                up=list(filter(lambda x:x.isupper(),psd))          # up=Upper(psd)

                if up and k and l:
                    if age>=18:
                        uns.append(us)
                        return func(us,psd,age)
                    else:
                        return "Age must be greater than 18"
                else:
                    return "Invalid Password"

            else:
                return "Minimum length of the password 8 characters"
        else:
            return "Username already exists"

    return inner
@valid
def login(username,password,age):
    return f"{username}'s Register Successful"
print(login("Nikhil","Nikhil@2005",21))