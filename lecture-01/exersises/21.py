# This program converts minutes to a totalol number of hours and minutes

n1 = int(input("Enter 1-st number in minutes: ")) #150
n2 = int(input("Enter 2-nd number in minutes: ")) #25
n3 = int(input("Enter 3-d number in minutes: ")) #440

numbers = [n1, n2, n3]
for n in numbers:
    h = n // 60
    m = n - h * 60
    if h < 24:
        print(h, m)
    else:
        print("The given number of minutes can't be calculated.")     