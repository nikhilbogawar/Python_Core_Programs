# Write a program that opens a file in read mode, reads the first 10 characters,
# prints the current cursor position using tell(), moves the cursor back to the
# beginning using seek(0), and reads the full content again.

with open("data.txt","r") as f:
    print(f.read(10))
    print("Position:",f.tell())
    f.seek(0)
    print(f.read())