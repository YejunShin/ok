import turtle
user=int(input("how big is the circle?"))
def user_c():
	turtle.circle(user)
	turtle.penup()
	turtle.forward(user)

my_list=(5, 4, 3, 2, 1, 0)
for i in range(6):
	turtle.pendown()
	user_c()
	print(my_list)
	len(my_list)