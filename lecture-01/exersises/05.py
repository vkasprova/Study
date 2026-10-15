#This program converts distance in feet to inches, yards and miles

d_feet = float(input("Input distance in feet: "))

d_inches = int(d_feet * 12)
d_yards = d_feet * 0.333333333
d_miles = d_feet * 0.000189393939

print(f"The distance in inches is: {d_inches} inches.")
print(f"The distance in yards is: {d_yards} yards.")
print(f"The distance in miles is: {(round(d_miles,3))} miles.")