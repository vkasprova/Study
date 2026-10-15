#The program calculates what amount of money you will need to deposit to get the desired value in needed number of years.
f = float(input("Enter the desired future value: "))
r = float(input("Enter the annual interest rate: "))
n = float(input("Enter the number of years the money will grow: "))
p = float(f/(1+r)**n)
print(f"You will need to deposit this amount: {p:.2f}.")