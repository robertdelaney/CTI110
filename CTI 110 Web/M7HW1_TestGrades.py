# CTI-110
# M7HW1_TestGrades_RobertDeLaney.py
# Robert DeLaney
# 12-4-17


# Write a program that ask the user to calculate the
# test average and grade of five test scores
# conversion is total of five test scores /5

test1 = int(input('Enter score 1: '))
test2 = int(input('Enter score 2: '))
test3 = int(input('Enter score 3: '))
test4 = int(input('Enter score 4: '))
test5 = int(input('Enter score 5: '))

total =(test1 + test2 + test3 + test4 + test5)
            
# CalculateAverage
def calc_average(total):
            return total / 5
#Grade

def determine_score(grade):
    if 90 <= grade <= 100:
        return 'A'
    elif 80 <= grade <= 89:
        return 'B'
    elif 70 <= grade <= 79:
        return 'C'
    elif 60 <= grade <= 69:
        return 'D'
    else:
        return 'F'


grade = total
avg = calc_average(total)
abc_grade = determine_score(grade)

print("That's a(n): " + str(abc_grade))
print('Average grade is: ' + str(avg))



    




    
