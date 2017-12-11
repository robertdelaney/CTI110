# CTI-110
# M5HW2_SoftwareSales_DeLaney
# Robert DeLaney
# 13-11-17

# Get number of packages
total = int(input('Enter number of packages purchased' ))

# if subtotal = $99 * number of packages
if total > 10:
    print ('$99 * 10 packages purchased' )
    print ('Discount is 10%' )
if total > 20:
    print ('$99 * 20 packages purchased' )
    print ('Discount is 20%' )
if total > 30:
    print ('$99 * 50 packages purchased')
    print ('Discount is 30%' )

if total > 100:
    print ('$99 * 100 packages purchased' )
    print ('Discount is 40% ')
else: 
    print ('$99 * 9 packages purchased' )
    print ('Discount is 0' )




    


