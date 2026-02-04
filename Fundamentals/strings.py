# strings are either in 'here' or "here"
string1 = "pankaj1"
string2 = 'pankaj2'
print(string1)
print(string2)

# quotes inside quotes -> we can write quotes inside quotes as long as the don't match
string3 = "hey I'm 'Pankaj'"
print(string3)

string4 = 'hey I am "Pankaj"'
print(string4)

# we can write multiple lines in a string using three quotes
string5 = '''pankaj
wrote this in 
three quotes'''
print(string5)

string6 = """pankaj 
wrote this again in 
three quotes"""
print(string6)

# String as arrays -> strings are usable in the form of arrays
str1 = "this is a string"
print(str1[0])
print(str1[3])
print(str1[5])
print(str1[0])

# looping through a string
for char in str1:
    print(char, end = " ")

print()

# to get the length of a string we use len(string_here)
print(len(str1)) # len = 16

# to check if a certain word is in string or not we dd
str2 = "pankaj singh rawat"
print("pankaj" in str2) # returns True

# what if I dont wanna return true and just wanna print something on my own ?
if("rawat" in str2):
    print("Rawat was here")

# to check if a certain character is not in string we use -> not in
print("pankaj" not in str2) # returns False


## String Slicing -> variable[start:finish]
st1 = "pankaj singh rawat"

# slice from start 
print(st1[0:6]) # returns pankaj
print(st1[:6]) # this also returns pankaj

# slice to end
print(st1[7:])
print(st1[7:len(st1)])

# negative indexing
print(st1[-5:-2])

# modifying strings
print(st1.upper())
print("PSR".lower())

# remove white spaces from starting and ending -> strip()
print(" who is PSR?   ".strip())

# replacing strings
print("pankaj".replace('a', 'A'))

# to split strings -> split()
st3 = "okay! man"
print(st3.split('!'))

st4 = "pankaj, singh, rawat"
print(st4.split(','))

# concatenation of strings -> +
a1 = "hey"
a2 = "there"
a3 = "man"
print(a1+ " " + a2+ " " + a3)

# format strings -> f-strings or format()
"""
this cannot be done down below:
age = 36
txt = "My name is Pankaj, I am " + age
print(txt)
This will produce an error:
cuz both the data tpes are of different type
so we use f-strings or format()
"""
age = 22
txt = f"My name is Pankaj, I am {age}" # this is how we use f-strings 
print(txt)

# lets say I want a print which is in int to appear in float upto 4 deciaml points then 

price = 50
a2 = f"this costs {price:.4f}" # variable_name:.till_which_decimal_placef
print(a2)

# we can even do this 
b2 = f"this is the price of 2 bags {500 * 2}"
print(b2)

# Escape characters

# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value


# String Methods
'''
capitalize()	Converts the first character to upper case
casefold()	Converts string into lower case
center()	Returns a centered string
count()	Returns the number of times a specified value occurs in a string
encode()	Returns an encoded version of the string
endswith()	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	Searches the string for a specified value and returns the position of where it was found
format()	Formats specified values in a string
format_map()	Formats specified values in a string
index()	Searches the string for a specified value and returns the position of where it was found
isalnum()	Returns True if all characters in the string are alphanumeric
isalpha()	Returns True if all characters in the string are in the alphabet
isascii()	Returns True if all characters in the string are ascii characters
isdecimal()	Returns True if all characters in the string are decimals
isdigit()	Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	Returns True if all characters in the string are lower case
isnumeric()	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	Returns True if all characters in the string are whitespaces
istitle()	Returns True if the string follows the rules of a title
isupper()	Returns True if all characters in the string are upper case
join()	Joins the elements of an iterable to the end of the string
ljust()	Returns a left justified version of the string
lower()	Converts a string into lower case
lstrip()	Returns a left trim version of the string
maketrans()	Returns a translation table to be used in translations
partition()	Returns a tuple where the string is parted into three parts
replace()	Returns a string where a specified value is replaced with a specified value
rfind()	Searches the string for a specified value and returns the last position of where it was found
rindex()	Searches the string for a specified value and returns the last position of where it was found
rjust()	Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	Splits the string at the specified separator, and returns a list
rstrip()	Returns a right trim version of the string
split()	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()	Returns a trimmed version of the string
swapcase()	Swaps cases, lower case becomes upper case and vice versa
title()	Converts the first character of each word to upper case
translate()	Returns a translated string
upper()	Converts a string into upper case
zfill()	Fills the string with a specified number of 0 values at the beginning
'''