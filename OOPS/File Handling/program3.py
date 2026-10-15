# Write a program that creates a file and writes 3 lines using write(), reopens
# the same file in append mode, appends 2 more lines, and finally reads and prints
# the complete file content.

with open("data.txt","w") as f:
    f.write("First\nSecond\nThird\n")
with open("data.txt","a") as f:
    f.write("Fourth\nFifth")
with open("data.txt","r") as f:
    print(f.read())