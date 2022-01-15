""""Chapter 5 examples and exercises"""

# Exercise 5.6

# 5.6.1

import turtle 

def koch(t, length):
    if length<20:
        t.fd(length)
        return
    m=length/3
    koch(t,m)
    t.lt(60)
    koch(t,m)
    t.rt(120)
    koch(t,m)
    t.lt(60)
    koch(t,m)
    
curve=turtle.Turtle()

koch(curve, 300)

turtle.mainloop()
turtle.bye()
