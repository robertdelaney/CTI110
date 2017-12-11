# CTI-110
# M6T1B: Initials
# Robert DeLaney
# 11-29-17


import turtle
wn=turtle.Screen()
R = turtle.Turtle()

#add display options
R.pensize(3)
R.pencolor("green")
R.shape("turtle")


R.left(90)
R.forward(50)
R.right(90)
R.forward(50)
R.right(90)
R.forward(25)
R.right(90)
R.forward(40)
R.left(90)
R.left(45)
R.forward(35)

# Move to New Spot
R.penup()
R.right(125)
R.backward(145)
R.left(180)
R.pendown()

# Draw Second Initial
R.right(90)
R.forward(100)
R.left(90)
R.circle(50,180)
R.hideturtle()

# end command
wn.mainloop()








