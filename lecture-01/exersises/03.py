# Calculation parameters of a circle
import math
print("This program is calculating the area and the circumference of a circle.")
r = float(input("Enter radius of the circle: "))
S = math.pi * r**2
L = math.pi*2*r
print(f"Area of a circle: {S}")
print(f"Circumference: {L}")
