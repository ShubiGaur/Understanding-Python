# Another thing to know about indexing is range. 

# Say I want to return multiple items in a list.

# EXAMPLE: Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"] # << The search will start at index 2 (included) and end at index 5 (not included).
print(thislist[2:5])

# Try leaving out the start value and see what happens
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])

# OR instead, leave out the end value
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

# You can also specify ranges for negative indexes:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

