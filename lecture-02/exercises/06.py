# This program calculates EMI

# Import the Decimal class from the decimal module
from decimal import Decimal, getcontext
# set precision
getcontext().prec

def EMI_find(P, r, n):
    # Convert to Decimal
    P = Decimal(P)
    r = Decimal(monthly_rate)
    n = Decimal(n)
    EMI = P * ( r * (1 + r) ** n) / ((1 + r) ** n - 1)
    EMI = EMI.quantize(Decimal('0.000000000001'))
    return EMI

# Pab, pmir, tnmp = input("Enter principal amount borrowed, periodic monthly interest rate, total number of monthly payments: ")
Pr_amout = input("Enter principal amount borrowed: ")   #Princiapl amount borrowed
annual_rate = input("Enter interest rate per year: ")   #Periodic monthly interest rate
number_paym = input("Total number of monthly payments: ")   #Total number of monthly payments

monthly_rate = Decimal(annual_rate) / Decimal(12 * 100)  # місячна ставка

result = EMI_find(Pr_amout, monthly_rate, number_paym)
print(f"EMI for {number_paym} months: {result}")