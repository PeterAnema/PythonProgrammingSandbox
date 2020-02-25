import turtle
turtle.home()

n = 4
angle = 180 - (360 / n)

# for i in range(4):
#     turtle.forward(250)
#     turtle.left(90)

# for i in range(50):
#     turtle.forward(250)
#     turtle.right(144)


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

input('Close?')