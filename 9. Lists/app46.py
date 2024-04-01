# To change an item value in a list, you just need to refer to the index number.
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant" # << call the index number and then set it equal to what you want to replace it with
print(thislist) # << should print "blackcurrant" instead of "banana"

# The exact same logic can be applied to a range of values! Look below:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"] # << range of values instead of just one
print(thislist)

"""
If you insert more items than you replace, the new items will be inserted 
where you specified, and the remaining items will move accordingly

If you insert less items than you replace, the new items will be inserted 
where you specified, and the remaining items will move accordingly

"""