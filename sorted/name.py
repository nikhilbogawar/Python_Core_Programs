names = ["Nikhil", "Tejas", "Bharath", "Vishal", "Naresh", "Srikanth", "Ganesh"]
print(sorted(names, key=len))
print(sorted(names, key=lambda x: x[0])) #using lambda function with sorted() function (only this line code)