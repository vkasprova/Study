# This program creates a new string from three middle symbols of the entered string.
str1 = input("Enter string: ") # JhonDipPeta, JaSonAy
mid_ind = len(str1) // 2 # Find index of middle symbol

mid1 = str1[mid_ind-1]
mid2 = str1[mid_ind]
mid3 = str1[mid_ind+1]

print(mid1+mid2+mid3)