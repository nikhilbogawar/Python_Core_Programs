marks=[35,15,24,11,36,49,21,33,17,36]
def check(m):
    return m>=25
print(list(filter(check, marks)))
print(list(filter(lambda m: m>=25, marks))) #using lambda funtion with filter() function (only this line code)