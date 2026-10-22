# This program checks if the entered string is palindrome.
str1 = input("Enter string: ")

if str1 == str1[::-1]:  # Compare the string with its reversed slice.
    print("The entered string is palindrome.")
else:
    print("The entered string isn't palindrome.")


# 2-d way not so good)
#lenght = len(str1)
#if lenght % 2 == 0:
#    lenght1 = str1[:lenght // 2] #Take the first part of string
#    lenght2 = str1[lenght // 2:] #Take the second part of string
#    if lenght1 == lenght2[::-1]:
#        print("The entered string is palindrome.")
#    else:
#        print("The entered string isn't palindrome.")
#elif str1 == str1[::-1]:
#    print("The entered string is palindrome.")
#else:
#    print("The entered string isn't palindrome.")