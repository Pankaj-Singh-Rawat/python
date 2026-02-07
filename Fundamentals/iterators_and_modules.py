import testFun # importing own module
from testFun import dict1 # importing dict from the module
testFun.printvalue()

# An iterator is an object that contains a countable number of values.

arr = ["apple", "banana", "cherry"]
ans = iter(arr)
print(next(ans))
print(next(ans))
print(next(ans))

# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
# To prevent the iteration from going on forever, we can use the StopIteration statement.

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 10:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
  print(x)

print(dict1["name"]) # calling dictionary from a module