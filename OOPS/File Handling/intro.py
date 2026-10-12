# f=open("test.txt","r")
# print(f.read())# full file text
# f.seek(0)#f.tell()
# print(f.readline())#
# f.seek(0)
# print(f.readlines())
# f.seek(0)
# file=open("test1.txt","x")
# file.truncate(10)

# with open('test.txt', 'w+') as f,open('test.txt', 'a') as g:
#     f.write('Hello World')
#     f.seek(0)
#     print(f.read())
#     f.write("test")
#     f.close()
#     g.write('Hello World\n')
#     g.write("test")

# to create context manager we use two methods
# by using class
class A:
    def __init__(self,fn):
        self.fn=fn
    def __enter__(self):
        print("Entering the file.....")
        self.f=open(self.fn,'r')
        return self.f
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Closing the file.....")
        self.f.close()
obj=A("test.txt")
with obj as f:
    print(f.read())

# by using context library importing
import contextlib
@contextlib.contextmanager
def f(fn):
    print("Entering the file.....")
    x=open(fn,'r')
    try:
        yield x
    finally:
        print("Closing the file......")
        x.close()

with f("test.txt") as f:
    print(f.read())