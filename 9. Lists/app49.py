# What about removing?

# The remove() method removes the specified item.

# EXAMPLE: Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") # << remove() used
print(thislist)

# If there are more than one item with the specified value, the remove() method removes the first occurance:
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

# If you want to quickly remove a specific item, use pop()

# EXAMPLE: Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1) # << pop() used
print(thislist)