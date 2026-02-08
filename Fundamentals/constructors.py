import cowsay
class MyClass:
    name = None
    tyre = None

    def __init__(self, name , tyre):
        self.name = name
        self.tyre = tyre

    def callOne(self):
        return cowsay.cow(self.returnName() + " Yohoooooo!")
    
    def returnName(self):
        return self.name

# child class of MyClass
class YourClass(MyClass):
    pass

class Lastclass(YourClass):
    pass
p1 = MyClass("BMW" , 4)
print(p1.name)
print(p1.tyre)

print(p1.callOne())



class ThisClass:
    name = None

    def __init__(self): # paramters
        pass


C1 = ThisClass()
C1.name = "pankaj"
print(C1.name)
