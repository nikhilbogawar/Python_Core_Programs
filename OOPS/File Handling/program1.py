# Write a Python program using a context manager (with) to open a text file in
# read mode, read the entire content using read(), and print the number of
# characters in the file.

with open("data.txt","r") as f:
    content=f.read()
    print("Characters:",len(content))