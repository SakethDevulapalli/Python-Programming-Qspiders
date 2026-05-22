num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))
num3 = int(input("Enter the third number : "))

if num1 > num2 and num1 > num3 :
    if num2 > num3 :
        print(num2, "is greatest number..")
    else :
        print(num3, "is greatest number..")
elif num2 > num3 and num2 > num1 :
    if num1 > num3 :
        print(num3, "is greatest number..")
elif num3 > num1 and num3 > num2 :
    if num2 > num1 :
        print(num3, "is greatest number..")