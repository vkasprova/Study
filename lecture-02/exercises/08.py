# This program calculates the area of a triangle by given base and height using Decimal and function.

# Import the Decimal class from the decimal module
from decimal import Decimal, getcontext
# set precision
getcontext().prec = 10

def s_triangle(b, h):
    """Finding the area of triangle by given base and height"""
    b = Decimal(b)
    h = Decimal(h)
    S = b * h / 2
    return S

base = input("Enter base of triangle, cm: ")
height = input("Enter height of triangle, cm: ")

result = s_triangle(base, height)

print(f"The area of triangle is: {result} cm^2")