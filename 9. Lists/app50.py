# The del keyword also removes the specified index:
thislist = ["apple", "banana", "cherry"]
del thislist[0] # << del() used
print(thislist) # << should just print ['banana', 'cherry']

# The del keyword can also delete the list completely:
del thislist

# The clear() method empties the list. The list still remains, but it has no content.
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)


