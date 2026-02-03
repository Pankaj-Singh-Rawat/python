# A variable is created the moment you assign a value to it. 
# no need to write data type
x = 5 # int data type
y = "pankaj" # String data type
print(x)
print(y)

x = 23.34 # float data type
print(x)

print()

# assigning multiple variables
x,y,z = "pankaj", "singh", "rawat"
print(x)
print(y)
print(z)

print()

# one value to multiple variables
x = y = z = "Demon"
print(x)
print(y)
print(z)

print()

# unpacking a collection: if you have a pack of tuple, list etc you can put it in variables
fruits = ["pankaj", "singh", "rawat"]
x,y,z = fruits
print(x)
print(y)
print(z)