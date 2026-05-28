# count = int(input("Enter number of vehicles : "))
# petrol = 500

# for i in range(1, count+1) :
#     liter = int(input("Enter the amount of liters : "))
#     print("vehicle",i, " Filled", liter, "liters")
#     petrol = petrol - liter
# print("The total amount of petrol remaining is : ", petrol)

'''
Petrol pump fuel filling
Vehicles arrive one by one at a petrol station.
Record fuel filled for each vechicle until the total fuel sold reaches 500 liters
#Updates are there
'''
# data = []
# i = 0
# while i < 500 :
#     fuel = int(input("Enter the amount liters : "))
#     if fuel > 0 :
#         data.append(fuel)
#         i += fuel
#         if fuel > 500 :
#             print("There is limit petrol")
#     else :
#         print("Negative petrol is entered.")

# if i == 500 :
#     print("Out of fuel")
#     print("The records of sold petrol are", data)


'''
Hospital patient temperature check
A hospital records temperature of patients entering the emergency ward. Stop when a patient with temperature above 104f is found and display the paitent count checked before that.
'''
# ward = []
# while True :
#     person = int(input("Enter the temperature of the patient : "))
#     if person > 104 :    
#         print("You will not enter the ward.")
#         break
#     ward.append(person)

# print(ward)
# print(len(ward))


'''
Website login attempt system
A user has only three attempts to enter the correct password. Display "Access Granted" if correct, otherwise block the account.
'''
# password = 1443
# count = 3
# for i in range(count) :
#     user = int(input("Enter the password : "))
#     if user == password :
#         print("Access Granted")
#         break
#     elif user != password :
#         print("Wrong password..")


'''
WAP that keeps asking the user for a number until they enter 0, then prints the sum of all entered numbers
'''

'''
Sum of digits until single digits
keeps summing the digits of a number until the result is a single digit. Example : 98765 -> 9+8+7+6+5 = 35 -> 3+5 = 8. use a loop
'''
# num = int(input("Enter a number : "))
# while num > 10 :
#     result = 0
#     temp = num
#     while temp != 0 :
#         last_digit = temp % 10
#         result += last_digit
#         temp //= 10
#     print(result)
#     num = result



'''
Collatz sequence
Start with any positive interger N. If even, divide by 2; if odd, multiply by 3 and add 1. Repeat until you reach 1. Print the sequence length.
'''

'''

'''