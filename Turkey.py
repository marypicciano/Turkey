import turtle
t = turtle.Turtle() #functions within the library
s = turtle.getscreen

def feather(r, angle, color): #function for feathers
    for i in range(2): #multiple feathers
        turtle.fillcolor(color)
        turtle.begin_fill()
        turtle.circle(r, angle)
        turtle.left(180-angle)
        turtle.end_fill()
    return 

def brown_feathers(r=300, angle=90, n=7): #specific color for feathers
    for i in range(n):
        feather(r, angle, "brown")
        turtle.left(15)
    return

def orange_feathers(r=200, angle=90, n=5): #specific color for feathers
    for i in range(n):
        feather(r, angle, "orange")
        turtle.left(15)
    return

brown_feathers()
orange_feathers()

#body
t.up()
t.goto(0,-10)
t.down()
t.pen(pencolor='black', fillcolor='yellow', pensize=5, speed = 9)
t.begin_fill()
t.circle(80)
t.end_fill()


#head
t.up()
t.goto(0,140)
t.down()

t.pen(pencolor='black', fillcolor='yellow', pensize=5, speed = 9)
t.begin_fill()
t.circle(40)
t.end_fill()

#left eye
t.up()
t.goto(-10, 180)
t.down()

t.pen(fillcolor='black', pensize=1, speed=9)
t.begin_fill()
t.circle(5)
t.end_fill()


#right eye
t.up()
t.goto(10, 180)
t.down()
t.pen(fillcolor='black', pensize=1, speed=9)
t.begin_fill()
t.circle(5)
t.end_fill()

#right leg
t.up()
t.goto(10,0)
t.down()
t.pen(fillcolor='black', pensize=5, speed=9)
t.right(90)
t.forward(40)

#right toe
t.up()
t.goto(10,-40)
t.down()
t.left(45)
t.forward(10)

#middle toe
t.up()
t.goto(10,-40)
t.down()
t.right(45)
t.forward(10)

#left toe
t.up()
t.goto(10,-40)
t.down()
t.right(45)
t.forward(10)

#left leg
t.up()
t.goto(-10,0)
t.down()
t.pen(fillcolor='black', pensize=5, speed=9)
t.left(45)
t.forward(40)

#right toe
t.up()
t.goto(-10,-40)
t.down()
t.left(45)
t.forward(10)

#middle toe
t.up()
t.goto(-10,-40)
t.down()
t.right(45)
t.forward(10)

#left toe
t.up()
t.goto(-10,-40)
t.down()
t.right(45)
t.forward(10)

t.setheading(0)

#hat
t.up()
t.goto(60,220)
t.down()
t.backward(120)

t.up()
t.goto(40,220)
t.down()

t.pen(pencolor='black', fillcolor='black', pensize=1, speed=9)
t.begin_fill()
t.left(90)
t.fd(40)
t.left(90)
t.fd(80)
t.left(90)
t.fd(40)
t.end_fill()

