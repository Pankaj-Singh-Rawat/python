# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.

myTuple = (1,2,3,122323, "pankaj", "pankaj")
print(myTuple)

print(myTuple[len(myTuple) - 1])

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

# Technique - Change Tuple Values
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

# add items
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# add tuple to a tuple
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y

print(thistuple)

# remove values from tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)

# Unpacking a Tuple
fruits = ("apple", "banana", "cherry")
x, y, z = fruits
print(x)
print(y)
print(z)

print()

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
x, y, *z = fruits
print(x)
print(y)
print(z)

# multiply by 2
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)


# methods
'''
count()	Returns the number of times a specified value occurs in a tuple
index()	Searches the tuple for a specified value and returns the position of where it was found
'''