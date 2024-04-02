# You can customize your own sort function.
# For that, use the argument: key = function

# EXAMPLE: Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)



