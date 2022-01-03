""""Chapter 4 examples and exercises"""

# 4.3. Exercises

import turtle

# 2


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


bob = turtle.Turtle()
square(bob, length=200)

turtle.mainloop()
turtle.bye()
