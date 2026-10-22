# This program prints the 1-st, middle and the last symbol of a string for a given word
str1 = input("Enter a word with an odd number of letters: ") #James

first = str1[0] # Find the 1-st symbol
mid_ind = len(str1) // 2 # Find index of middle symbol
mid = str1[mid_ind] # Find middle symbol
last = str1[-1] # Find the last symbol

print(first+mid+last)