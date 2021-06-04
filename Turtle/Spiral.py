import turtle
t1 = turtle.Turtle()
t1.speed(0)
forward = 1

while True:
    t1.forward(forward)
    t1.left(120)
    t1.left(1)
    forward = forward + 1
turtle.done()