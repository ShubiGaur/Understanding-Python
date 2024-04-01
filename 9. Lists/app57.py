# Expressions are the current item but also outcome. Basically, they're like methods that help enhance the list to your liking.
# Examples might help you understand better:

# EXAMPLE: Set the values in the new list to upper case:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x.upper() for x in fruits]
print(newlist)

# Check another example:

# EXAMPLE: Set all values in the new list to 'hello':
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = ['hello' for x in fruits]
print(newlist)

# The expression can also contain conditions:

# EXAMPLE: Return "orange" instead of "banana":

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)




