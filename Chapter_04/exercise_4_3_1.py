""""Chapter 4 examples and exercises"""

# 4.3. Exercises

import turtle

# 1


def square(t):
    for i in range(4):
        t.fd(100)
        t.lt(90)


bob = turtle.Turtle()

square(bob)

turtle.mainloop()
turtle.bye()
