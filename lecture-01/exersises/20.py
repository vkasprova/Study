# This program converts seconds to a totalol number of days, hours, minutes, seconds

s1 = int(input("Enter 1-st number in seconds: ")) #6785
s2 = int(input("Enter 1-st number in seconds: ")) #456789
s3 = int(input("Enter 1-st number in seconds: ")) #86401

seconds = [s1, s2, s3]
for s in seconds:
    d = s // 86400
    h = (s - d * 86400) // 3600
    m = (s - d * 86400 - h * 3600) // 60
    sec = s - d * 86400 - h * 3600 - m * 60
    print(f"{s} seconds is: {d} day(s), {h} hour(s), {m} minute(s), {sec} second(s).")    


#if s1 / 86400 >= 86400:
#    d1 = s1 // 86400
#else: d1 = 0    