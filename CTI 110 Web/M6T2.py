# CTI-110
# M6T2Lab_DeLaney.py
# Robert DeLaney
# 12-1-17

# Set total = 0
# for each of 7 days:
# Input bugs collected for a day
# Add Bugs collected to total
#
# Initialize the accumulator
total = 0

# Get the bugs collected for each day.
for day in range (1,8):
    #Prompt the user
    print('Enter the bugs collected on day', day)

    #Input the number of bugs
    bugs = int(input('How many bugs were collected on this day? '))

    #Add bug to total
    total = total + bugs

#Display the total bugs.
print ('You collected a total of', total, 'bugs. ')
