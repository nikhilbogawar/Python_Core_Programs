salary = [10000,24000,65000,14500,31000]
def increment(x):
    return x+2000
updated_list=list(map(increment, salary))
print(updated_list)   
print(list(map(lambda x: x+2000, salary)))    #using labmda function with map() function (only this line code)