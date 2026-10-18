# This program calculates net salary 
s = float(input("Enter your salary: "))
t = float(input("Enter tax in %: "))

ns = s - (s * t) / 100

print(f"Your net salary is: {ns}")