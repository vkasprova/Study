# This program converts days, hours, minutes, seconds to a total number of seconds

d = int(input("Days: "))
h = int(input("Hours: "))
m = int(input("Minutes: "))
s = int(input("Seconds: "))

total_seconds = d * 86400 + h * 3600 + m * 60 + s

print(f"The amounts of seconds: {total_seconds}.")