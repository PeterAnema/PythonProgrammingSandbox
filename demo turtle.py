# demo turtle

import turtle

turtle.home()
turtle.pendown()

turtle.goto(100, 0)
turtle.goto(100, 100)
turtle.goto(0, 100)
turtle.goto(0, 0)

turtle.penup()

pad = ['l',50,'l',50,'l',50,'l',50]

turtle.reset()
turtle.pendown()
for stap in pad:

    if stap == 'l':
        turtle.left(90)
    elif stap == 'r':
        turtle.right(90)
    else:
        turtle.forward(stap)

turtle.penup()

        
