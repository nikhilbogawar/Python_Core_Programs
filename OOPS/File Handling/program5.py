# • Create a custom context manager using a class that opens a file in write mode
# in the __enter__ method, writes a line to the file, closes the file in the
# __exit__ method, and properly prints or logs any exception information received
# in __exit__.

class FileManager:
    def __enter__(self):
        self.f=open("data.txt","w")
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()
        if exc_type:
            print("Exception:",exc_val)
        return False
with FileManager() as f:
    f.write("Python is a High level language and also an interpreted language...")