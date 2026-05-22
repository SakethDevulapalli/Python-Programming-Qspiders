'''
A user enters a weekday(Monday to sunday). If it is a weekday(mon-fri), ask for number of hours worked. If hours > 40, pay = hours * 100 + (hours - 40) * 50 (overtime). Else pay = hours * 100. For weekdays (sat-sun), pay = hours * 150, If entered invalid day, print error. Complete and print total pay.
'''

weekday = int(input("1. Monday \n"
"2. Tuesday \n"
"3. Wednesday \n"
"4. Thrusday \n"
"5. Friday \n"
"6. Saturday \n"
"7. Sunday \n"
"Choose a Day : "))
pay = 0
hours = int(input("Enter the no. hours you worked : "))
if weekday in [1, 2, 3, 4, 5] :
    if hours > 40 :
        pay = hours * 100 + (hours - 40) * 50
    else :
        pay = hours * 100
    print("The pay you got is :", pay) 
elif weekday in [6, 7] :
    pay = hours * 150
    print("The pay you got is :", pay)
else :
    print("Invalid day...")