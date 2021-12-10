""""Chapter 2 examples and exercises"""

# 2.6 String operations

# The + operator performs string concatenation, which means it joins the strings by linking them end-to-end. For example:
first = 'throat'
second = 'warbler'
print(first + second)  # should print 'throatwarbler'

# The * operator also works on strings; it performs repetition.
# For example, 'Spam'*3 is 'SpamSpamSpam'.
# If one of the values is a string, the other has to be an integer.

print('Spam'*3)
print(3*'Spam')


# 2.10 Exercises

# Exercise 2.1

# n = 42 is a legal expression. What about 42 = n ?
# print(42=n) # returns a syntax error

# How about x = y = 1 ?
# print(x=y=1) # returns a synax error

# In some languages every statement ends with a semi-colon, ;.
# What happens if you put a semi-colon at the end of a Python statement?
# print("test") ; # returns a syntax error

# What if you put a period at the end of a statement?
# print("test").  # returns a syntax error

# In math notation you can multiply x and y like this: xy.
# What happens if you try that in Python?
# x = 1
# y = 2
# print(xy) # returns a name error: NameError: name 'xy' is not defined
