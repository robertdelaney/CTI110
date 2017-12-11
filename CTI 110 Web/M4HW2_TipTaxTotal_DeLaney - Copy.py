# CTI-110
# M4HW2 - Tip Tax Total
# Robert DeLaney
# 08-11-17

# Enter the charge for food
tipRate=0.18
taxRate=0.07

# Get the cost of the meal
mealcost = float(input('How much was the cost of your meal? '))

# Calculate the amount of tip
tip = mealcost * tipRate

# Calculate the amount of tax
tax = mealcost * taxRate

#Display the total cost of the meal
total = mealcost + tax + tip


print('Mealcost' , format(mealcost, '0.02f'))
print('Tax total', format(tax, '0.2f')) 
print('Tip total', format(tip, '0.2f')) 
print('Meal total',format(total,'0.2f'))

