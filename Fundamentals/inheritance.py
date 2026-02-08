class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def __str__(self):
    return f"Your name is {self.firstname} {self.lastname}"

#Use the Person class to create an object, and then execute the printname method:

x = Person("pankaj", "rawat")
print(x.__str__())


class childClass(Person):
    def __init__(self, fname, lname, age = 18):
        super().__init__(fname,lname)
        self.age = age
    
    def __str__(self):
        return f'Your name is {self.firstname} {self.lastname}, I am {self.age}'



y = childClass("baccha", "1")
print(y.__str__())
