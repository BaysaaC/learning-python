""""Chapter 3 examples and exercises"""

# 3.14 Exercises

# 3.1 Write a function named right_justify that takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.


def right_justify(string):
    string_length = len(string)
    justify_length = 70-string_length
    print(justify_length*" "+string)


right_justify("hello")

# 3.2.1


def do_twice(f):
    f()
    f()


def print_spam():
    print("spam")


do_twice(print_spam)

# 3.2.2


def do_twice_v2(f, value):
    f(value)
    f(value)

# 3.2.3


def print_twice(bruce):
    print(bruce)
    print(bruce)

# 3.2.4


do_twice_v2(print_twice, "SPAM")

# 3.2.5


def do_four(f, value):
    do_twice_v2(f, value)
    do_twice_v2(f, value)


do_four(print, "SPAAAAM")


# 3.3.1

def print_border(n_columns):
    print('+ - - - - '*n_columns, end='')
    print('+')


def print_entry(n_columns):
    print('|         '*n_columns, end='')
    print('|')


def print_columns(n):
    print_border(n)
    do_four(print_entry, n)


def print_grid(x, y):
    i = 0
    while i < y:
        print_columns(x)
        i = i+1
    print_border(x)


print_grid(5, 3)
