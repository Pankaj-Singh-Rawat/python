# positional args
def my_function(name, /):
  print("Hello", name)

# my_function(name = "pankaj") -> this wont work 
my_function("pankaj") # this works

# Keyword args
def my_function(*, name):
  print("Hello", name)

my_function(name = "pankaj")

# Arbitary Arguments -> *args
'''
If you do not know how many arguments will be passed into your function, add a * before the parameter name.

This way, the function will receive a tuple of arguments and can access the items accordingly
'''

# Arbitrary Keyword Arguments - **kwargs
def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "pankaj", lname = "rawat")


# function inside a funtion
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()


# nonlocal keyword : The nonlocal keyword makes the variable belong to the outer function.
def myfunc1():
  x = "Jane"
  def myfunc2():
    nonlocal x
    x = "hello"
  myfunc2()
  return x

print(myfunc1())

# Decorator -> must have a unner funtion to wrap logic in inner function
def changecase(func):
    def wrapper1():
        return func().lower()
    return wrapper1

@changecase
def myfunction():
  return "Hello Sally"

print(myfunction())

# Argument based Decorator:
def changecase(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@changecase(1)
def myfunction():
  return "Hello Linus"

print(myfunction())

# Function Metadata
# a function's name can be returned with the __name__ attribute
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# a decorators name can be returned with functools.wraps
import functools

def changecase(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase
def myfunction():
  return "Have a great day!"

print(myfunction.__name__)

# lambda
def newFun(a):
  return a * 2
x = lambda a : a*2

print(newFun(2))
print(x(2))

def my_generator():
  yield 1
  yield 2
  yield 3

for value in my_generator():
  print(value)