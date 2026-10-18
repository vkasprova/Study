# This program finds number of km by given distance

n1 = int(input("Enter 1-st distance in m: "))
n2 = int(input("Enter 2-nd distance in m: "))
n3 = int(input("Enter 3-d distance in m: "))

dist = [n1, n2, n3]
for d in dist:
    res = d // 1000
    print(f"In {d} m number of km is: {res}")



# 2-d way to calculate
#km = 1000

#def calc_dist(n1, km):
#    dist = n1 // km
#    return dist
#res = calc_dist(n1, km)
#print(res)

#n1 = n2
#res = calc_dist(n1, km)
#print(res)

#n1 = n3
#res = calc_dist(n1, km)
#print(res)    