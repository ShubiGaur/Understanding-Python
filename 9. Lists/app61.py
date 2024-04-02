# You cannot copy a list simply by typing list2 = list1, because: 
# list2 will only be a reference to list1
# changes made in list1 will automatically also be made in list2.

# To copy...just use copy()
# Shocking, amirite?

# EXAMPLE: Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list().

# EXAMPLE: Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist) # << Yields the same result as the last one, right?





