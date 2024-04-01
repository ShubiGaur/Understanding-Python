# More about list comprehension:

# It offers a shorter syntax when you want to create a new list based on the values of an existing list.

# See the following example to understand more clearly:

# EXAMPLE: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# This is the long way of doing it.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehension, you can do it on one line of code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x] # << condensed for loop
print(newlist)



# Confused on the syntax?

"""
newlist = [expression FOR item IN iterable IF condition == True]

"""