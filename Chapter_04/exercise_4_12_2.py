""""Chapter 4 examples and exercises"""

# 4.12 Exercises 

# Exercise 2

import math 
import turtle

def arc(turtle, radius, angle):
    arc_length=2*math.pi*radius*angle/360
    n_steps=int(arc_length/30)+3
    step_length = arc_length / n_steps
    step_angle = angle / n_steps
    
    for i in range(n_steps):
        turtle.fd(step_length)
        turtle.lt(step_angle)


def petal(turtle, radius, angle):
    for i in range(2):
        arc(turtle, radius, angle)
        turtle.lt(180-angle)
        
def flower(turtle, radius, angle, petals):
    for i in range(petals):
        petal(turtle, radius, angle)
        turtle.lt(360/petals)

        
baby = turtle.Turtle()

flower(baby, radius=200, angle=25, petals=25)

turtle.mainloop()
turtle.bye()


