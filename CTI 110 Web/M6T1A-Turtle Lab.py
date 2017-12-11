# CTI-110
# M6T1-Turtle Lab
# Robert DeLaney
# 11-29-17

import turtle
win = turtle.Screen()
r = turtle.Turtle()

for x in range(2):
    r.forward(100)          
    r.left(120)
r.forward (100)
r.penup()
r.forward (100)
r.pendown()

for x in range(4):
    r.forward(50)          # Tell alex to move forward by 50 units
    r.left(90)
           
win.mainloop()
