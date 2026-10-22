# This program checks symmetry of string

str1 = input("Enter string: ") #khokho
lenght = len(str1) # Lenght of string

if lenght % 2 == 0: 
    lenght1 = str1[:lenght // 2] #Take the first part of string
    lenght2 = str1[lenght // 2:] #Take the second part of string

    if lenght1 == lenght2: # Check if the first and second parts of string are symmetrical
        print("The entered string is symmetrical.")
    else:
        print("The entered string isn't symmetrical.")
else:
    print("The string length is odd, so symmetry cannot be checked.")