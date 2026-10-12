# 3. Create two Python modules that import each other. Run the program to observe
# what happens with circular imports. Then think of different ways to prevent a
# circular-import crash.
import module_b
def show_a():
    print("Module A")
if __name__=="__main__":
    show_a()
    module_b.show_b()