#WAP TO FIND THE ANGLE FROM THE GIVEN SIDE OF THE TRIANGLE
import math

a,b,c=input("Enter the side  of the triangle with space").split(' ')
a,b,c=int(a),int(b),int(c)
a_= (math.acos((((b**2)+(c**2))-(a**2))/(2*b*c)));
b_= (math.acos((((a**2)+(c**2))-(b**2))/(2*a*c)));
c_= (math.acos((((a**2)+(b**2))-(c**2))/(2*a*c)));
print (a_)
print(b_)
print(c_)