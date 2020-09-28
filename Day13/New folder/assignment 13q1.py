x1=int(input("enter x coordinate of first circle: "))
x2=int(input("enter x coordinate of second circle: "))
y1=int(input("enter y coordinate of first circle: "))
y2=int(input("enter y coordinate of second circle: "))
r1=int(input("enter radius of first circle: "))
r2=int(input("enter radius of second circle: "))
if (((x2-x1)**2)+((y2-y1)**2))**0.5 == (r1+r2):
    print("the circles touch each other")
elif (((x2-x1)**2)+((y2-y1)**2))**0.5 < (r1+r2):
    print("the circles intersect")
else:
    print("the circles do not intersect")