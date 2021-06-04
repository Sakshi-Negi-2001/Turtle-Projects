import turtle
t1 = turtle.Turtle()

def main():
    
    t1.shape("turtle")
    t1.up()
    
    draw_circle(1,-50,"green",60)
    draw_circle(300,300,"orange",60)
    draw_circle(-300,300,"blue",60)
    draw_circle(-300,-350,"red",60)
    draw_circle(300,-350,"yellow",60)



def draw_circle(x,y,color,rad):
    t1.speed(2)
    t1.goto(0,0)
    t1.goto(x,y)
    t1.down()
    t1.begin_fill()
    t1.fillcolor(color)
    t1.circle(rad)
    t1.end_fill()
    t1.up()
    t1.home()

if __name__ == '__main__':
	main()

