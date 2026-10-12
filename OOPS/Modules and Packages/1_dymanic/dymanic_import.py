# write a python program that attempts to dynamically import a module at runtime. the program should only
# import the module if it actually exists; otherwise, it should print "Module does not exist"
import importlib.util
import importlib
name=input("Enter module name: ")
if importlib.util.find_spec(name):
    module=importlib.import_module(name)
    print("Module imported successfully")
else:
    print("Module does not exist")