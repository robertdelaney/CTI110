# CTI-110
# M7T1_Delaney.py Kilometer Converter
# Robert DeLaney
# 12-4-17


# Write a program that ask the user to enter a distance
# in Kilometers, and then converts that distance to miles
# Formula Miles = Kilometers * 0.6214 



def askUserForKilometer():
    userKilometers = float(input('Enter distance in kilometers. '))
    return userKilometers

def convertKilometersToMiles (userKilometers ):
    miles = userKilometers * 0.6214
    return miles

def main():
    userTypedKilometers = askUserForKilometer() 
    convertedMiles = convertKilometersToMiles (userTypedKilometers )
    print(userTypedKilometers,'Kilometers converted to miles is',\
          format (convertedMiles, '.2f') + 'miles. ')



main()
