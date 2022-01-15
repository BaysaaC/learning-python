""""Chapter 5 examples and exercises"""

# Exercise 5.5

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)

fractal=turtle.Turtle()
draw(fractal, 20, 5)

turtle.mainloop()
turtle.bye()



