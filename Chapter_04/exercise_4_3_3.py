""""Chapter 4 examples and exercises"""

# 4.3. Exercises

import turtle
import math

# 3


def polygon(t, length, n):
    for i in range(n):
        t.fd(length)
        t.lt(360/n)


bob = turtle.Turtle()

side = 200
polygon(bob, length=side, n=4)


# 4


def circle(t, r):
    perimeter = 2*math.pi*r
    n = 100
    length = perimeter/n
    polygon(t, length, n)


chris = turtle.Turtle()
chris.fd(side/2)
circle(chris, r=100)


# 5

def polyline(t, length, n, m):
    for i in range(m):
        t.fd(length)
        t.lt(360/n)


def arc(t, r, angle):
    perimeter = 2*math.pi*r
    n = 100
    m = int(100*angle/360)
    length = perimeter/n
    polyline(t, length, n, m)


dave = turtle.Turtle()
dave.fd(side/4)
arc(dave, r=100, angle=180)


turtle.mainloop()
turtle.bye()
