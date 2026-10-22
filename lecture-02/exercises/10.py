# This program calculates the area of a triangle using Heron's formula and the perimeter.
# 
import math 

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
u = input("Enter the unit of measurement: ")

P = a + b + c
s = P / 2
A = math.sqrt(s * (s-a) * (s-b) * (s-c))

print(f"The area of the triangle is: {A} {u}^2")
print(f"The perimeter of the triangle is: {P} {u}")


# a < b + c
# b < a + c
# c < a + b
