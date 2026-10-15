# Write a program that opens a file using a context manager, reads all lines
# using readlines(), and prints only the lines that contain more than 10
# characters.

with open("data.txt","r") as f:
    lines=f.readlines()
    for l in lines:
        if len(l)>10:
            print(l,end="")