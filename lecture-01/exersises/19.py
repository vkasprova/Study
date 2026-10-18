# The program calculates what amount of money you will get in 1 year by given deposit and interest rate in %.

d = float(input("Enter what amount of money you want to deposit: "))
r = float(input("Enter the annual interest rate: "))

d_in_1_Year = d + (d * r) / 100

print(f"You will get this amount: {d_in_1_Year}")