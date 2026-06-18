#  Create a function display_tags(**kwargs) that prints each keyword-value pair on its own line. 
def display_tags(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display_tags(name="Nikhil", age=21, branch="CSE", city="Hyderabad")