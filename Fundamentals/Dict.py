thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

newDict = {
    1: "pankaj",
    2: "singh",
    3: "rawat"
}

print(thisdict.get("year"))
print(len(thisdict))

print(newDict.values())

print(newDict.keys())
newDict.update({1: "psr"})

print(newDict.values())

newDict[4] = "name"
print(newDict.values())
newDict.update({5: "is"})
print(newDict.values())

newDict.pop(5)
newDict.popitem()


del newDict[2]

print(newDict.values())

for x in newDict.values():
    print(x)

print()

for x,y in newDict.items():
    print(x,y)
'''
Method	Description
clear()	Removes all the elements from the dictionary
copy()	Returns a copy of the dictionary
fromkeys()	Returns a dictionary with the specified keys and value
get()	Returns the value of the specified key
items()	Returns a list containing a tuple for each key value pair
keys()	Returns a list containing the dictionary's keys
pop()	Removes the element with the specified key
popitem()	Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	Updates the dictionary with the specified key-value pairs
values()	Returns a list of all the values in the dictionary
'''
