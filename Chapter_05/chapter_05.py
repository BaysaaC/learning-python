""""Chapter 5 examples and exercises"""

# 5.8 Recursion

def countdown(n):
    if n<=0:
        print("Blastoff !")
        return
    print(n)
    countdown(n-1)

countdown(5)

# 5.9. Stack diagrams for recursive functions

def print_n(string,n):
    if n<=0:
        return
    print(string)
    print_n(string, n-1)

print_n("hello",3)

def print_world():
    print("world")

def do_n(f,n):
    if n<=0:
        return
    f()
    do_n(f,n-1)

do_n(print_world,3)

# 5.11 Keyboard input

name=input("What is your name ?\n (Type here:)")

print("Hello,", name, "!")






















