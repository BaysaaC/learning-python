""""Chapter 5 examples and exercises"""

# Exercise 5.4

def recurse(n,s):
    if n == 0:
        print(s)
    else:
        recurse(n-1,n+s)
    
recurse(3,0)

"""
Stack diagram:
    __main__ : 
    recurse: n -> 3 ; s -> 0
    recurse: n -> 2 ; s -> 3
    recurse: n -> 1 ; s -> 5
    recurse: n -> 0 ; s -> 6
    recurse: n -> 0 ; s -> 6
"""

# 5.4.1 

recurse(-1,0)

"""
Stack diagram:
    
    __main__ :
    recurse: n -> -1 ; s -> 0
    recurse: n -> -2 ; s -> -1
    recurse: n -> -3 ; s -> -3
    recurse: n -> -4 ; s -> -6
    recurse: n -> -5 ; s -> -10
    ...
    no base case, infinite recursion, runtime error
    
"""

# 5.4.2

""" a recursive function which starts a countdown at 'n' and with a start 's'.
    'n' and 's' are summed at each iteration.
    When countdown is over, the function prints the incremented 's'
    'n' should be a positive integer. 

"""
