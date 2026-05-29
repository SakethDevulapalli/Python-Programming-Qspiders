'''
Petrol Pump Fuel Filling
Vehicles arrive one by one at a petrol station.
Record fuel filled for each vehicle until the total fuel
sold reaches 500 liters.
'''


##data=[]
##i=0
##while i<=500:
##        fuel=int(input('Enter the fuel in ltr: '))
##        i+=fuel
##        if i>500:
##            break
##        else:
##            data.append(fuel)
##
##print(data)

'''
Hospital Patient Temperature Check
A hospital records temperatures of patients entering
the emergency ward. Stop when a patient with temperature
above 104°F is found and display the patient count checked
before that.
'''


##count=0
##while True:
##    temp=int(input('Enter the temp: '))
##    if temp>104:
##        break
##    count+=1
##
##print(count)
'''
Website Login Attempt System
A user has only 3 attempts to enter the correct password.
Display "Access Granted" if correct, otherwise block the account.
'''
##psd=1234
##for i in range(3):
##    pd=int(input('Enter password: '))
##    if pd==psd:
##        print('Access granted')
##        break
##    else:
##        print('Wrong password')
    


'''
Write a program that keeps asking the user for a number
until they enter 0, then prints the sum of all entered numbers.

'''
##sum=0
##while True:
##    num=int(input('Enter the number: '))
##    if num==0:
##        print(sum)
##        break
##    else:
##        sum+=num

'''
Sum of Digits Until Single Digit
      Keep summing the digits of a number until the result
      is a single digit. Example: 98765 → 9+8+7+6+5=35 → 3+5=8.
      Use a loop.

'''

n=int(input('Enter the number: '))

while n>=10:
    res=0
    temp=n
    while temp!=0:
        res+=temp%10
        temp//=10

    n=res
    
print(res)









