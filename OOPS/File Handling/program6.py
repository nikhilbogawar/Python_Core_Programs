# Create a custom context manager using @contextmanager from the contextlib
# module that opens a file, yields the file object, and ensures the file is closed
# even if an exception occurs.

from contextlib import contextmanager

@contextmanager
def open_file():
    f=open("data.txt","w")
    try:
        yield f
    finally:
        f.close()
with open_file() as f:
    f.write("To create a custom context manager we have to import the contextlib library...")