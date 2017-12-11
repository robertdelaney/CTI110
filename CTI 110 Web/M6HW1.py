# CTI-110
# M6HW1_DeLaney.py
# Robert DeLaney
# 12-1-17

# What is the speed of the vehicle in mph?
# How many hours did the vehicle travel?
# List the Distance Traveled for each hour traveled.

speed = int (input ('What is your speed? '))
startHour = (1)
endHour = int (input ('How long has the vehicle been traveling? '))
endHour = endHour + 1

#Print the table headings
print ('Hour\tDistance Traveled')
print ('------------------------')

distance = 0
# Print the distance traveled for each hour
for hours in range (startHour, endHour):
    distance = speed * hours
    print (hours, '\t', distance)

