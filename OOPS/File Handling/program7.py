# Write a program using a context manager that opens a file in read mode, uses a
# loop to read the file in small chunks (for example, 5 characters at a time),
# prints the cursor position after each read using tell(), uses seek() to move to
# a specific position, and continues reading from there.

with open("data.txt","r") as f:
    while True:
        chunk=f.read(5)
        if not chunk:
            break
        print(chunk)
        print("Position:",f.tell())
    f.seek(3)
    print("From position 3:",f.read())