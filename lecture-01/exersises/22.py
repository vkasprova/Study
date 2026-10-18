# This program calculates days needed for trip by given numbers of km per day and total number of km needed for trip.
n = float(input("Enter number of km per day: ")) #600
m = float(input("Enter totalol number of km: ")) #625

d1 = m / 600
d2 = m // 600

if d1 == d2:
    print(f"You need {d1} days for your trip.")
else:
    print(f"You need {d2+1} days for your trip.")