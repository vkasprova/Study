# Calculating the hypotenuse of a triangle with given legs 0<a<=1000, 0<b<=1000
a=float(input("Enter 1-st leg: "))
b=float(input("Enter 2-d leg: "))
import math
if 0<a<=1000:
    if 0<b<=1000:
        print(math.sqrt(a**2+b**2))
    else: print("Error: the hypotenuse can't be calculated with given 2-nd leg.")
else: print("Error: the hypotenuse can't be calculated with given 1-st leg.")