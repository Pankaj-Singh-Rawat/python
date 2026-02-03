'''
str -> for text
int, float, complex -> for numeric
list, tuple, range -> for sequence
dict -> for mapping
set, frozenset -> for sets
bool -> for boolean
byte, bytearray, memoryview -> binary types
NoneType -> for None Type
'''

a = "hello world!"
print(a)

b = 20
print(a)

c = 3.14
print(c)

d = 1j
print(d)

e = ["pankaj", "singh", "rawat"]
print(e)

f = ("pankaj", "singh", "rawat")
print(f)

g = range(0, 12, 2) # starting point, last point, increment at each step
for i in g:
    print(i, end = " ")
print()

h = {"pankaj": 6, "singh":5 ,"rawat": 5}
print(h)

i = {"pankaj", "singh", "Rawat"}
print(i)

j = frozenset({"pankaj", "rawat"})
print(j)

k = True
print(k)

l = b"hello"
print(l)

m = bytearray(5)
print(m)

n = memoryview(bytes(5))
print(n)

o = None
print(o)