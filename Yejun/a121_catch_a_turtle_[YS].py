# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random
#-----game configuration----
t=trtl.Turtle()
score_writer=trtl.Turtle()
t.speed(0)
spot_color = "pink"
score=0
score_writer.speed(0)
#-----initialize turtle-----
t.shape("circle")
t.shapesize(2)
t.fillcolor("black")
score_writer.penup()
score_writer.goto(-380,290)
#-----game functions--------
def update_score():
	global score
	score+=1
	print(score)
def spot_clicked(x,y):
	xpos=random.randint(-400,400)
	ypos=random.randint(-300,300)
	t.penup()
	t.goto(xpos,ypos)
	update_score()
#-----events----------------
t.onclick(spot_clicked)



wn = trtl.Screen()
wn.mainloop()
