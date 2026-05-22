'''
A library charges a fine for late return:
    - Books returned within 5 days late : 2 rupees per day
    - 6-10 days late : 5 rupees per day
    - 11-15 days late : 10 rupees per day
    - Above 15 days late : 20 rupees per day plus a warning letter
    Take days late as input and complete fine.
'''

days = int(input("Enter the no. of days : "))
fine = 0
if days <= 5 :
    fine = days * 2
    print("Fine amount is :", fine)
elif 6<=days<=10 :
    fine = days * 10
    print("Fine amount is :",fine)
elif 11<=days<=15 :
    fine = days * 10
    print("Fine amount is :",fine)
else :
    fine = days * 20
    print("Warning Letter : You have taken the book for long long days...")
    print("Fine amount is :",fine)