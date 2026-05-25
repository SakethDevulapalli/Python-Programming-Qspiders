'''
Print :
*
* *
* * *
* * * *
* * * * *
'''

num = int(input("Enter a number : "))

# ##Left sided triangle
# for i in range(num) :
#     for j in range(i+1) :
#         print("* ", end = " ")
#     print()

# OR

# for i in range(1, num + 1) :
#     print("* " * i)

'''
        *
      * *
    * * *
  * * * *
* * * * *
'''

# ##Right sided triangle
# for i in range(1, num + 1) :
#     print("  " * (num-i) + " *" * i)


# ##Lefted sided reversed triangle
# for i in range(num, 0, -1) :
#     print("* " * i)


# ##right sided reversed triangle
# for i in range(num, 0, -1) :
#     print(" " * (num-i) + "*" * i)


# ##Unaligned Pyramid
# for i in range(1, num + 1) :
#     print(" " * (num-i) + "* "*i )


# ##unaligned Reverse pyramid
# for i in range(num, 0, -1) :
#     print(" " * (num-i) + "* "*i )


# ##Unaligned Diamond shape
# for i in range(1, num) :
#     print(" " * (num-i) + "* "*i )
# for i in range(num, 0, -1) :
#     print(" " * (num-i) + "* "*i )

# ##Pyramid shape
# for i in range(1, num + 1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1) )


# ##Reversed Pyramid shape
# for i in range(num, 0, -1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1) )


##Diamond shape
# for i in range(1, num + 1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1) )
# for i in range(num-1, 0, -1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1) )


# ##Left sided pyramid
# for i in range(1, num + 1) :
#     print("  "*(num-i) + "* " * i)
# for i in range(num-1, 0, -1) :
#     print("  "*(num-i) + "* " * i)


# ##Hollow daimond
# for i in range(1, num+1) :
#     if i==1 :
#         print("  " * (num - i) + " *")
#     else :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")
    
# for i in range(num-1, 0, -1) :
#     if i==1 :
#         print("  " * (num - i) + " *")
#     else :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")


# ##Hourglass
# for i in range(num, 0, -1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1))
# for i in range(2, num+1) :
#     print("  " * (num-i) + " *"*i + " *" * (i-1))


# ##Right sided pyramind
# for i in range(1, num + 1) :
#     print("* " * i)
# for i in range(num-1, 0, -1) :
#     print("* " * i)


# #Hollow Right Triangle
# for i in range(1, num+1) :
#     if i in [1, 2, num] :
#       print(" *" * i)
#     else :
#        print(" *" * 1 + "  " * (i-2) + " *")

# #Reverse Hollow Right Triangle
# for i in range(num, 0, -1) :
#     if i in [1, 2, num] :
#       print(" *" * i)
#     else :
#        print(" *" * 1 + "  " * (i-2) + " *")


##Hollow right sided triangle
# for i in range(1, num+1) :
#     if i in [1, 2] :
#       print(" *" * i)
#     else :
#        print(" *" * 1 + "  " * (i-2) + " *")
# for i in range(num, 0, -1) :
#     if i in [1, 2] :
#       print(" *" * i)
#     elif i != num:
#        print(" *" * 1 + "  " * (i-2) + " *")


# ##Hollow pyramid
# for i in range(1, num+1) :
#     if i in [1] :
#         print("  " * (num - i) + " *")
#     elif i != num :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")
#     else :
#        print(" *" * (i*2-1))

# print(" ", end="\n")

# ##Hollow Inverted pyramid
# for i in range(num, 0, -1) :
#     if i in [1] :
#         print("  " * (num - i) + " *")
#     elif i != num :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")
#     else :
#        print(" *" * i + " *" * (i-1))


# ##Square
# for i in range(1, num+1) :
#     print(" *" * num)

# ##Hollow Square
# for i in range(1, num+1) :
#     if i==1 :
#         print(" *" * (num*2))
#     else :
#         print(" *" * 1 + "  " * (num*2-2) + " *" * 1)
# for i in range(num-1, 0, -1) :
#     if i==1 :
#         print(" *" * (num*2))
#     else :
#         print(" *" * 1 + "  " * (num*2-2) + " *" * 1)


# ##Hollow Rectangle
# if num > 4 :
#     for i in range(1, num-3) :
#       if i==1 :
#           print(" *" * (num*2))
#       else :
#         print(" *" * 1 + "  " * (num*2-2) + " *" * 1)
#     for i in range(num-1, 0, -1) :
#         if i==1 :
#           print(" *" * (num*2))
#         else :
#           print(" *" * 1 + "  " * (num*2-2) + " *" * 1)
# else :
#    print("Enter a number which is greater than", num)


# ##Cross pattern( X )
# for i in range(num-1, 0, -1) :
#     if i==1 :
#         print("  " * (num - i) + " *")
#     else :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")
# for i in range(2, num) :
#     if i==1 :
#         print("  " * (num - i) + " *")
#     else :
#       print("  " * (num-i) + " *" + "  " * (2*i-3) + " *")

#OR

##Gives exact output for odd numbers only
# for i in range(1, num+1) :
#     for j in range(1, num+1) :
#         if i==j or i+j == num+1 :
#             print("*", end=" ")
#         else :
#             print(" ", end=" ")
#     print()