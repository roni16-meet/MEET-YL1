import turtle



turtle.getscreen().listen()
turtle.speed(0)

turtle.pencolor("red")
turtle.color("red")

def draw_circle(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.circle(10)
	turtle.end_fill()

def draw_square(x,y):
	turtle.penup()
	turtle.goto(x,y)
	turtle.pendown()
	turtle.begin_fill()
	turtle.goto(x+1,y)
	turtle.goto(x+1,y+1)
	turtle.goto(x,y+1)
	turtle.goto(x,y)
	turtle.end_fill()
def change_color_red():
	turtle.pencolor("red")
	turtle.color("red")


def change_color_random():
	turtle.pencolor("blue" or "red" or "pink" or "green" or "yellow" or "brown" or "black")

def change_color_blue():
	turtle.pencolor("blue")
	turtle.color("blue")
	
def change_color_white():
	turtle.pencolor("black")
	turtle.color("white")
	turtle.pensize(100)

turtle.onkeypress(change_color_red, "r")
turtle.onkeypress(change_color_blue, "b")
turtle.onkeypress(change_color_white, "w")
turtle.onkeypress(change_color_random, "k")
turtle.onscreenclick(draw_square, btn=3)



turtle.onscreenclick(draw_circle, add=True)



turtle.ondrag(turtle.goto, add=True)
turtle.ondrag(turtle.goto, btn=3, add=True)



turtle.pencolor("blue")
turtle.color("blue")



turtle.mainloop()
