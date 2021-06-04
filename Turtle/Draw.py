import turtle
t1 = turtle.Turtle()

move = 1

for i in range(360):
    t1.pendown()
    t1.right(move)
    t1.forward(100)
    t1.right(30)
    t1.forward(60)
    t1.left(30)
    t1.forward(30)
    t1.penup()
    t1.home()
    move = move+1
