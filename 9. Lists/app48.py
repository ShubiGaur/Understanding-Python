# Extending lists is the next topic, which is just appending elements from another list.

# EXAMPLE: Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist) 

# The extend() method does not have to append lists, you can add ANY iterable object (tuples, sets, dictionaries etc.).


