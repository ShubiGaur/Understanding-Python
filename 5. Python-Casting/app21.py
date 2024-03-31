# I touched on casting earlier...

# There may be times when you want to specify a type on to a variable. This can be done with casting. 

# Python is an object-orientated language, and as such it uses classes to define data types, including its primitive types.

# Casting is done using these functions:

int() 
# constructs an integer number from an integer literal OR
# constructs a float literal by removing all decimals OR
# constructs a string literal (providing the string represents a whole number)

float()
# constructs a float number from an integer literal OR
# a float literal OR
# a string literal (providing the string represents a float or an integer)

str()
# Constructs a string from a wide variety of data types, including strings, integer literals and float literals

# some examples with integers:

x = int(1)   # x will remain 1
y = int(2.8) # y will become 2
z = int("3") # z will become 3

# more examples with float:

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

# examples with strings:

x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'
