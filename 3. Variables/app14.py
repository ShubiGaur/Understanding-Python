# Global variables are created OUTSIDE of the function but can be used by anyone, both inside and outside of any given function.


# EXAMPLE: Create a variable outside of a function, and use it inside the function

x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. 
# The global variable with the same name will remain as it was, global and with the original value.
# See the example below and notice how it outputs two different things.


x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)


# To create a global variable INSIDE a function, you can use the 'global' keyword.

def myfunc():
  global x # <<<
  x = "fantastic"

myfunc()

print("Python is " + x)

