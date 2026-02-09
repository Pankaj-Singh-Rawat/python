# encapsulation -> to hide data from user
# you can make properties private by using a double underscore __ prefix
# getter and setter methods
class Person:

    def __init__(self, name, age):
        self.name = name
        self.__age = age # private cuz of __

    def __str__(self):
        return f"You are {self.name} & of age {self.__age}"

    def getAge(self): # getter method -> used to get private values
        return self.__age

    def setAge(self, age):
        self.__age = age


obj1 = Person("pankaj", 22)
print(obj1.__str__())
obj1.name = "ravida"
obj1.__age = 23 # nothing changes, why ? -> cuz age is private
print(obj1.__str__())
print(obj1.getAge())

obj1.setAge(23)
print(obj1.getAge())

# single underscore is used for protected variables/methods/classes -> _

