'''
Python Try Except
The try block lets you test a block of code for errors.
The except block lets you handle the error.
The else block lets you execute code when there is no error.
The finally block lets you execute code, regardless of the result of the try- and except blocks.
'''

# Exception Handling
try:
    print( 5 / 0)
except:
    print("error")

try:
    print("Cool")
except ArithmeticError:
    print("error")
except IndentationError:
    print("wrong Indentation")
else:
    print("This block is executed")
finally:
    print("This block will always execute")

n = 0
try:
    print( 10 / n)
except ArithmeticError:
    n += 2
    raise Exception("This is an Error")
finally:
    try:
        print( 10 / n)
    except: 
        print("Done")
    
    print("finally is completed")




