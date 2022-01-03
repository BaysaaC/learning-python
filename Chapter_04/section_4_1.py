""""Chapter 4 examples and exercises"""

# -*- coding: utf-8 -*-

# 4.1. The turtle module
import turtle

bob = turtle.Turtle()
print(bob)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(100)
bob.lt(90)

bob.fd(110)

# 4.2. Simple repetition
for i in range(4):
    bob.fd(100)
    bob.lt(90)

turtle.mainloop()
turtle.bye()
