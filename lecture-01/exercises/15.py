# This program calculates distance in 6, 10 and 15 hours by given speed.
v = float(input("Enter speed km/h: "))
times = [6, 10, 15]
for t in times:
    s = v * t
    print(f"In {t} hours, the car will cover a distance {s} km.")