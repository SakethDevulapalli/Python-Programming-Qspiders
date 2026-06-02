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
# num = int(input("Enter a number : "))
# temp = num
# count = []

# while temp != 1 :
#     # print(temp)
#     count.append(temp)
#     if temp % 2 == 0:
#         result = temp // 2
#     else :
#         result = (temp * 3) + 1
#     temp = result
# count.append(temp)
# print(count)

'''
Generate the first 20 terms of the fibonacci sequence using a loop. Store them in a list and then print the list. Also print the sum of all even-valued terms in the sequence.
'''
# n1 = 0
# n2 = 1
# result = []
# for i in range(20) :
#     result.append(n1)   #It prints the fibonacci sequence
#     n3 = n1 + n2
#     n1, n2 = n2, n3
# sum = 0
# arr = []
# for i in range(len(result)) :
#     if result[i] % 2 == 0 :
#         sum += result[i]    #It prints the sum of the even fibonacci sequence
#         arr.append(result[i])   #It prints the even fibonacci sequence
# print(arr)
# print(sum)


'''
The manager wants to identify all unique groups of three departments where the final net result is zero. This means the profit and loss values balance each other perfectly
WAP to find all unique triplets from the list whose sum is 0.
'''

# arr = [2, 0, -2, 3, -6, -3, -1, -2]
# res = []

# for i in range(len(arr)) :
#     for j in range(i+1, len(arr)) :
#         for k in range(j+1, len(arr)) :
#             if arr[i]+arr[j]+arr[k] == 0 :
#                 coll = [arr[i], arr[j], arr[k]]
#                 coll.sort()
#                 if coll not in res :
#                     res.append(coll)
# print(res)




# list = eval(input("Enter a list : "))
# target = int(input("Enter a number : "))
# res = []
# for i in range(len(list)) :
#     for j in range(i+1, len(list)) :
#         if list[i]+list[j] == target :
#             coll = [list[i], list[j]]
#             # coll.sort()
#             res.append(coll)

#OR

# for i in list :
#     if target-i in list :
#         coll = [i, target-i]
#         coll.sort()
#         if coll not in res :
#             res.append(coll)
# print(res)


'''
WAP to check whether the list contains any subarray whose sum is equal to the target value. 
'''
# list = [3, 4, -2, 5, 1, -3]
# target = 7
# res = []
# for i in list :     #This code is for only subarray which length is 2. Need to do with different length of subarrays.
#     if target-i in list :
#         coll = [i, target-i]
#         res.append(coll)
#         if (i+target-i) == target :
#             print("True")
#             break
# print(res)

#OR

# list = [3, 4, -2, 5, 1, -3]
# target = 7
# flag = False
# for i in range(len(list)) :
#     sum = 0
#     sum += list[i]
#     for j in range(i+1, len(list)) :
#         sum += list[j]
#         if sum == target :
#             flag = True
#             break
# print(flag)


'''
Given a list of numbers. Create another list having len as 3 where 1st elements is the sum of prime numbers present, second element is the no of prime numbers and third element is the no. of composite numbers.
'''
# list = [2, 7, 9, 3, 4, 1]
# def is_prime(num) :
#     if num <= 1 :
#         return False
#     for i in range(2, num) :
#         if num % i == 0 :
#             return False
#     return True

# sum_prime = 0
# count_prime = 0
# count_comp = 0

# for i in list :
#     if is_prime(i) :
#         sum_prime += i
#         count_prime += 1
#     else :
#         if i == 1 :
#             continue
#         else :
#             count_comp += 1
# result = [sum_prime, count_prime, count_comp]
# print(result)


'''
A company gives performance points to employees.
The HR manager wants to identify all employee pairs where one employee is points exactly double the other employee's score.
WAP to find all such pairs from the list.
'''
# score = [2, 4, 6, 8, 3, 12]
# res = []
# for i in score :
#     d = i*2
#     if d in score :
#         pair = [i, d]
#         pair.sort()
#         if pair not in res :
#             res.append(pair)
# print(res)


'''
WAP to find the kth rotation of a list
'''
# list = [1, 2, 3, 4, 5]
# rotation = int(input("Enter a number for rotation : "))
# for i in range(rotation) :
#     el = list.pop()
#     list.insert(0, el)
#     print(list)


'''
A company stores product codes as strings.
Sometimes the same code is entered in rotated form

ex: "ABCD" rotated becomes "BCDA"
    "ABCD" rotated becomes "CDAB

The manager wants to find all pairs of strings where one string is a rotation of another.
Write a python program to find all such pairs.
'''

'''
Rock Paper Scissor for five rounds
'''


'''
Armstrong Number
'''
# num = int(input("Enter a number : "))
# def is_armstrong(num):
#     result = 0
#     while num != 0 :
#         digit = num % 10
#         new_num = digit * digit * digit
#         result = (result * 10) + new_num
#         num //= 10
    
#     return if True result == num else False
# print(is_armstrong(num))      #needed to correct


'''
Neon Number
Write a function is_neon() that checks if a number is a neon number(sum of digits of its square equals the number itself)
'''
# num = int(input("Enter a number : "))
# def neon_number(num) :
#     result = 0
#     while num != 0 :
#         result += (num%10) ** 2
#         num //= 10
#     return True if num == result else False
# print(neon_number(num))       #needed to correct


'''
Write a function is_spy() that checks if a number is a spy number (sum of digits equals product of digits)
'''
# num = int(input("Enter a number : "))
# def is_spy(num) :
#     temp = num
#     sum = 0
#     prod = 1
#     while temp != 0 :
#         sum += temp % 10
#         prod *= temp % 10
#         temp //= 10
#     return sum == prod
# print(is_spy(num))



'''
WAF is_duck() that checks if a number is a duck number(contains at least one zero, but does not start with zero)
'''
# num = input("Enter a number : ")
# def is_duck(num):
#     digits = num
#     if '0' in digits and digits[0] != 0:
#         print(True)
#     else :
#         print(False)
# is_duck(num)



'''
WAF is_magic() that checks if a number is a magic number(recursively summing digits until single digits results in 1)
'''
# num = int(input("Enter a number : "))
# def is_magic(num):
#     while num >= 10 :
#         result = 0
#         while num != 0 :
#             result += num % 10
#             num //= 10
#         num = result
#     return True if result == 1 else False
# print(is_magic(num))


'''
WAF is_palindrome
'''
# num = int(input("Enter a number : "))
# def is_palindrome(num):
#     result = 0
#     while num != 0:
#         new_num = num % 10
#         result = result * 10 + new_num
#         num //= 10
#         print(result)
#     return True if num == result else False
# print(is_palindrome(num))     #needed to correct



'''
WAF is_automorphic()
'''
num = int(input("Enter a number : "))
# def is_automorphic(num):
#     new_num = num * num
#     print(new_num)
#     power = len(str(num))
#     if (new_num % (10 ** power) == num):
#         print(True)
#     else:
#         print(False)

#OR

# def is_automorphic(num):
#     sqr = num * num
#     # print(sqr)
#     power = 0
#     while num != 0:
#         power += 1
#         num //= 10
#     new_number = sqr % (10 ** power)
#     # print(new_number)
#     return num == new_number      #needed to correct

print(is_automorphic(num))