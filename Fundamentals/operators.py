# Arithmatic Operators 

x = 15
y = 2

print(x+y)
print(x-y)
print(x*y)
print(x/y) # return floating value
print(x//y) # return integer value
print(x%y) # remainder
print(x**y)


# Assignment Operators: =, +=, -=, *=, /=, %=, //=, **=, &=, ^=, >>=, <<=, :=

x /= 3 # x = x / 3
print(x)

y **= 3
print(y)

a = 5
a &= 3 # a = a & 3 -> 101 & 011 -> 001
print(a)

# if you want to swap two numbers without using a 3rd variables
# ex-or operation
x1 = 1 # 001 
x2 = 4 # 100 

x1 = x1^x2 # 101: 5
x2 = x1^x2 # 101^100: 001
x1 = x1^x2  # 101^001: 100
print(x1, x2)

# right shift
x3 = 4 # 100
x3 >>= 1 # -> 10 -> 2
print(x3)

# left shift
x4 = 45 # 101101
x4 <<= 4 # 1011010000
print(x4)

# walrus operator 

''' 
Normal approach:

line = input("Enter a command ('quit' to stop): ")
while line != "quit":
    print(f"You said: {line}")
    line = input("Enter a command ('quit' to stop): ")

Cooler approach:
while(line := input("Enter a command ('quit' to stop): ") != 'quit'):
    print(f"You said: {line}")
    line = input("Enter a command ('quit' to stop): ")

'''



# Comparison operators: ==, !=, >, <, >=, <=

# Logical operators: and, or, not
x5 = 12
print(not(x5 > 3 and x5 < 20))

# Membership operators: in, not in
newList = []
for i in range (0,10,2):
    newList.append(i)
    print(i, end = " ")

print()
print()
print(newList)
print(1 not in newList)

print()
list = ["pankaj", "singh", "rawat"]
print("pankaj" not in list)

print(~3) # plus 1 and sign change -> positive numbers as input
print(~-12) # minus 1 and sign change -> negative numbers as input