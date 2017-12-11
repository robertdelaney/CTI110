# CTI-110
# M7T2_FeetToInches_RobertDeLaney.py
# Robert DeLaney
# 12-4-17
 
# Write a program that ask the user to enter a number
# feet, and then converts that number to inches
# conversion formula is one foot equals 12 inches


def askUserForFeet():
    userFeet = float(input('Enter distance in feet. '))
    return userFeet

def convertFeetToInches (userFeet ):
    inches = userFeet * 12
    return inches

def main():
    userTypedFeet = askUserForFeet()
    convertedInches = convertFeetToInches (userTypedFeet )
    print(userTypedFeet,'Feet converted to inches is',\
          format (convertedInches, '.2f') + 'inches. ')

main()
