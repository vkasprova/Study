#This program converts height in feet and inches to centimetres

h_feet = int(input("Feet: "))
h_inches = int(input("Inches: "))

h_cm = h_feet * 30.48 + h_inches * 2.54

print(f"Your height is: {h_cm} cm.")