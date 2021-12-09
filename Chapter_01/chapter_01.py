""""Chapter 1 examples and exercises"""

# 1.3 First program
print('Hello, world !')

# 1.4 Arithmetic operators
print(40+2)
print(43-1)
print(6*7)
print(84/2)
print(6**2+6)

# 1.5 Values and types
print(type(2))
print(type(42.0))
print(type('Hello, world !'))
print(type('42.0'))
print(1, 000, 000)
# 1,000,000 is not a legal integer in Python, but it is legal
# (Python interprets it as a comma-separated sequence of integers)


# 1.9 Exerices

# Exercice 1.1
print(-2)
print(+2)
print(3++2)  # legal expression that returns a value, here equal to integer 5
# print(011)  returns a syntax error: "leading zeros in decimal integer literals are not permitted"
# print(2 3)  returns a syntax error.


# Exercice 1.2

# 1. Number of seconds in 42 minutes and 42 seconds ?
print(42*60+42)

# 2. Number of miles in 10 km ? (Hint: 1 mile = 1.61 km)
print(10/1.61)

# 3. If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per mile in minutes and seconds)? What is your average speed in miles per hour?

print(((42*60+42)/(10/1.61))/60)
print(((10/1.61)/((42*60+42))*3600))
