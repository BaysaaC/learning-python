""""Chapter 3 examples and exercises"""

# 3.1 Function calls

# Python provides functions to convert values from one type to another.

# The int function takes any value and converts it to an integer, if it can, or complains otherwise:
print(type('42'))
print(type(int('42')))
# print(int('Hello')) # returns: ValueError: invalid literal for int() with base 10: 'Hello'

# int can convert floating-point values to integers, but it doesn’t round off; it chops off the fraction part:
print(int(3.99999))  # returns: 3

# float converts integers and strings to floating-point numbers:
print(float(42))  # returns 42.0
print(float("3.14159"))  # returns: 3.14159

# Finally, str converts its argument to a string:

print(str(32))  # returns: '32'
print(str(3.14159))  # returns: '3.14159'
print(type(str(3.14159)))  # returns: <class 'str'>
