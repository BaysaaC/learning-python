""""Chapter 3 examples and exercises"""

# 3.2 Math functions

# Before we can use the functions in a module, we have to import it with an import statement:
import math

# This statement creates a module object named math.
# If you display the module object, you get some information about it:
print(math)  # returns: <module 'math' (built-in)>

# The module object contains the functions and variables defined in the module.
# To access one of the functions, you have to specify the name of the module and the name of the function, separated by a dot (also known as a period).
signal_power = 2
noise_power = 1
ratio = signal_power / noise_power

decibels = 10*math.log10(ratio)
