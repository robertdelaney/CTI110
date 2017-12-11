# CTI-110
# M6T1CLAB_DeLaney.py
# Robert DeLaney SnowFlake(bonus)
# 12-1-17

import turtle
wn =turtle.Screen()
d =turtle.Turtle()

# add some display options
#d.pensize(3)
d.pencolor("Orange")
d.shape("turtle")


# Create my shape
for i in range (20):
    for i in range(2):
        d.forward(100)
        d.right(60)
        d.forward(100)
        d.right(120)
        # Rotate
        d.right(18)

wn.exitonclick()


