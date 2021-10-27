import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "arrow", "turtle", "circle", "square", "triangle", "classic"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "red", "blue", "green", "orange", "purple", "gold"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  my_turtles.append(t)
t_forward=50
t_right=0
t_thick=0
startx = t.xcor()
starty = t.ycor()
t.speed(0)
for t in my_turtles:
	t.pensize(t_thick)
	t.penup()
	new_color = turtle_colors.pop()
	t.fillcolor(new_color)
	t.pencolor(new_color)
	t.left(45)
	t.goto(startx, starty)
	t.pendown()  
	t.right(t_right)   
	t.forward(t_forward)
	t.penup()
	startx = t.xcor()
	starty = t.ycor()
	t_right+=45
	t_forward+=10
	t_thick+=2
wn = trtl.Screen()
wn.mainloop()