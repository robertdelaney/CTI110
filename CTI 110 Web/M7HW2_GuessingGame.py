# CTI-110
# M7HW2_GuessingGame_RobertDeLaney.py
#Robert DeLaney
# 12-4-17

# Write a program that ask the user to guess
# the random number between 0-50 if the answer is false
# the program will instruct the user to try again higher or lower
# if user guess is true the program will print ("Well Done")
# and print("End of program") will end the session

import random
randomNumber = random.randrange (0,50)
print('Random number has been generated')
guessed = False
while guessed==False:
    userInput = int(input('Your guess please: '))
    if userInput==randomNumber:
        guessed = True
        print('Well done!!')
    elif userInput>50:
        print('Our guess range is between 0 and 50, try a little lower')
    if userInput<0:
            print('Our guess range is between 0 and 50, try a little higher')
    elif userInput>randomNumber:
            print('Try again, a little lower')
    elif userInput<randomNumber:
            print('Try again, a little higher')


print ('End of program')
        
