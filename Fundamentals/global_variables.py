''' 
Global variables: are created outside of a function(method) -> all variables created till now were global

Global variables can be used by anyone and anywhere, meaning global variables can be used by methods and functions
'''

x = "global method"

def myfunc():
    print("this is a " + x)

myfunc()

# what if we use global variable inside method?

def newMethod():
    x = "local method"
    print("this is a " + x) # we will se the local method is being used, then how do we use global methods?
    print("this is a " + globals()['x']) # this is how gloaba; variables are accessed using global keyword

newMethod()

# what if I define a variable in method that I wanna access gloabally?

def method1():
    global x # to set it to global we write global in front of x, we also use global to change the value of already defined variable
    x = "local method which is now global" 
    print(x)

method1()


