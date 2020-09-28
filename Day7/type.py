#WAP TO FIND THE ANGLE FROM THE GIVEN SIDE OF THE TRIANGLE
import math

a,b,c=input("Enter the side  of the triangle with space       ").split(' ')
a,b,c=int(a),int(b),int(c)
a_= math.degrees(math.acos((((b**2)+(c**2))-(a**2))/(2*b*c)));
b_= math.degrees(math.acos((((a**2)+(c**2))-(b**2))/(2*a*c)));
c_= math.degrees(math.acos((((a**2)+(b**2))-(c**2))/(2*a*c)));
print(round(a_),"degree")
print(round(b_),"degree")
print(round(c_),"degree")


