"""
age = 36
txt = "My name is John, I am " + age
print(txt)

"""

# Just like we discussed earlier, the code above would NOT run because we cannot combine strings and numbers. Not like this.

# But we CAN combine strings and numbers by using the format() method!
# This method takes passed arguments > formats them > places them in the string where '{}' are:

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age)) 

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))