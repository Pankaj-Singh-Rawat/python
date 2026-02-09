 # CRUD -> Create, Read, Update, Delete
 # The open() function takes two parameters; filename, and mode.
"""
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists

In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode

"b" - Binary - Binary mode (e.g. images)
"""

f = open("/Users/psr/Documents/python/Fundamentals/new.txt")
print(f.readline())
print(f.read(5))

print(f.read())

# using with statement
with open("/Users/psr/Documents/python/Fundamentals/new.txt") as f:
    print(f.read())

# to close file we use -> f.close()
f.close()


"""
Write to an Existing File
To write to an existing file, you must add a parameter to the open() function:
"a" - Append - will append to the end of the file
"w" - Write - will overwrite any existing content
"""

with open("/Users/psr/Documents/python/Fundamentals/new.txt", 'a') as f: # a -> append
    f.write("This is the last appended line")

# to create a new file
f = open("openFile.txt", "x")

