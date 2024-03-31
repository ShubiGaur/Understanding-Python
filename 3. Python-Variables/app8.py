# Variables are containers for storing data values, just like in any other language.

# Variables do not need to be declared with any particular type, and can even change type after they have been set. For example:

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)


# If you want to specify the data type, this can be done with casting.

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Lastly, you can get the datatype by calling the type() function.

x = 5
y = "John"
print(type(x))
print(type(y))