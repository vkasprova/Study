# This program calculates the area of a triangle using Heron's formula
# 
import math 

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
u = input("Enter the unit of measurement: ")

s = (a + b + c) / 2
Ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

print(f"The area of the triangle is: {Ar} {u}^2")