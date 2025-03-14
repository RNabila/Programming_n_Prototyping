#nabila raisa 01 and 02. 03-14-2025

import turtle

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.forward(length * n) 
    t.left(angle) 
    draw(t, length, n-1) 
    t.right(2 * angle)
    draw(t, length, n-1) 
    t.left(angle) 
    t.backward(length * n) 

def square(t):
   
    for _ in range(4):
        t.forward(100) 
        t.left(90) 


bob = turtle.Turtle()


draw(bob, 10, 4)  

#no overlapping
bob.penup()
bob.goto(-50, -50) #diff pos
bob.pendown()


square(bob)


turtle.done()
