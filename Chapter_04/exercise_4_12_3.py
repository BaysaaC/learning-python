""""Chapter 4 examples and exercises"""

# 4.12 Exercises 

# Exercise 3

import turtle 
import math

def slice(t, radius, angle, length):
    t.pd()
    t.fd(radius)
    t.lt(angle)
    t.fd(length)
    t.lt(angle)
    t.pu()
    t.fd(radius)
    t.lt(180)
    
def pie(t, radius, slices):
    length=2*radius*math.sin(math.pi/slices)
    interior_angle=360/slices
    angle=180-(180-interior_angle)/2
    for i in range(slices):
        slice(t, radius, angle, length)

    
bob=turtle.Turtle()
pie(bob, 100, 7)
        
turtle.mainloop()
turtle.bye()












