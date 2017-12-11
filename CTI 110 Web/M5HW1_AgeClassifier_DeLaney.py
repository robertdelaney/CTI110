# CTI-110
# M5HW1_AgeClassifier_DeLaney
# Robert DeLaney
# 13-11-17

# ask the persons age
age = int(input('The persons age.'))

# if the person is 1 or younger
if age <= 1:
          print ('The person is an infant.' )
# if the person is older than 1 but younger than 13
elif age > 1 and age < 13:
          print ('The person is a child.' )
# if a person is at least 13, but less than 20
elif age >=13 and age < 20:
          print ('The person is a teenager.' )
else:
    print ('The person is an adult.' )
