# Once a tuple is created, you cannot change its values. 

# But there is a workaround.

# You can convert the tuple into a list, change the list, and convert the list back into a tuple.

# EXAMPLE: Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x) # < converting to a list
y[1] = "kiwi"
x = tuple(y) # < converting back to tuple
print(x)

# To add items, follow the same premise. Convert it to a list, change the list, then back to a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)



