# The print function prints its parameter to standard out
# and appends a line seperator string to the end. 

print("Hello World ")

# The print method may print its parameter without appending
# a line seperator string to the end paramater.

print("Hello World", end="")
print("Hello World")

print(100)
print(True)
print(100.75)

# We can pass one or more parameters when using the print function.
# By default, they will be seperated by a space.

print(100, True, 100.75)

# The default space can be modificed and can be made to change to 
# any charactes, integer, or string using the sep parameter. 

print(100, True, 100.75, sep="-")

# the sep and end parameters may be used together in one print statement.

print(100, True, 100.75, sep="-", end="!")

# the string % modulo operator can be used with the print function
# for formatting.
print("\nHello %s %s you are %d years old." % ("Susan", "Ceklosky", 54))
print("Hello %s %s you are %.2f years old." % ("Susan", "Ceklosky", 54.5))

# The input function can be used to get data from standard in.
# the returned object will always be String.
first = input("Please enter your first name: ")
last = input("Please enter your last name: ")
print(first, last)

age = int(input("Please enter your age: "))
print("Hello %s %s. You are %s years old." % (first, last, age))
print("Hello %s %s. You are %.2f years old." % (first,last, age))

print(type(first), type(last), type(age))

# We must typecast the returned object if we want to work with
# it in a form other String
intage = int(input("Please enter your age: "))
print("Hello %s %s. You are %d years old." % (first, last, intage))

floatage = float(input("Please enter your age: "))
print("Hello %s %s. You are %.2f years old." % (first,last,floatage))

# The split function can be used to get multiple values from standard in.
# If a seperator isn't given to the function, then a white space is used.
fname, lname = input("Enter your first and last names seperated by a space: ").split()
print(fname, lname)

# A seperator, like a comma, may be provided
fname, lname, tn = input("Enter your first and last names and telephone seperated by a comma: ").split(",")
print("Hello %s %s. your phone number is %s." % (fname, lname, tn))


# We can take in a variable number of inputs at a time.
x = [int(x) for x in input("Enter multiple numbers seeprated by a space: ").split()]
print("Numbers are: ", x)    