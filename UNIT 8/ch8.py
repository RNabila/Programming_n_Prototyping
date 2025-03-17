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

def square(t,length):
   
    for _ in range(4):
        t.forward(length) 
        t.left(90) 


bob = turtle.Turtle()


draw(bob, 10, 4)  

#no overlapping
bob.penup()
bob.goto(-50, -50) #diff pos
bob.pendown()

square(bob,50)
square(bob,100)
square(bob,150)


turtle.done()
