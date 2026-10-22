# This program calculates compound interest

# Import the Decimal class from the decimal module
from decimal import Decimal, getcontext
# set precision
getcontext().prec = 10

def complex_interest(P, r, n, t):
    # Convert to Decimal
    P = Decimal(P)
    r = Decimal(r)
    n = Decimal(n)
    t = Decimal(t)
    A = P * (1 + (r / n)) ** (n * t)
    return A

Pr_amount = input("Enter principal amount: ")   # Principal amount (P)
int_rate = input("Enter annual interest rate: ") # Annual interest rate (r)
nt_int_per_year = input("Enter number of times interest is compounded per year: ") # Number of times interest is compounded per year (n)
years = input("Enter number of years for which the interest is calculated: ") # Number of years (t) for which the interest is calculated

final_interest = complex_interest(Pr_amount, int_rate, nt_int_per_year, years)
print(f"Final interest in {years} years: {final_interest.quantize(Decimal('.01'))}")