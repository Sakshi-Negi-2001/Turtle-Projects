import turtle
colors =['red','yellow','green','purple','blue','pink']
t1 = turtle.Pen()
turtle.bgcolor('black')

for i in range (500):
    t1.pencolor(colors[i%6])
    t1.width(i/100+1)
    t1.forward(i)
    t1.left(59)