
#functions allow you top break up your code

# creatre a function that says hi

def sayhi():
    print("Hello User")

    # (): = all the code that comes after this colon is part of the function
    # code that goes inside of a function needs to be indented
# next step is to call a function
print("Top")
sayhi()
print("bottom")
# create a function that passes a parameter

def sayhi2(name, age):
    print("Hello " + name + " you are " + age)

sayhi2("Mike", "35")
sayhi2("Steve", "42")