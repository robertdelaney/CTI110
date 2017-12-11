# CTI-110
# M6LAB_DeLaney.py
# Robert DeLaney
# 12-1-17

# Write a program that uses nested loops to draw this pattern:

# *******
# ******
# *****
# ****
# ***
# **
# *

for currentRow in range (7, 0, -1):
    for currentColumn in range( currentRow  ):
        print( "*", end=" " )
    print("")
