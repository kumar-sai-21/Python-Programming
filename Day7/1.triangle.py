#1. Write functions to do following:
#Take 3 sides of triangle as input and do following:
#i. Return True for a valid triangle sides else false
#ii. Classify the triangle as "Equilateral", "Rightangled", "Isosceles", "Scalene" (Default).
#iii. Provided the given sides are valid else return NotValid
#iv. Provided the triangle is "valid" and "Right angled" return the radius of circumcenter else return -1
#SAI KUMAR SATAPATHY

def is_valid(a,b,c):
    if((a+b)>c or (a+c)>b or (b+c)>a):
        return True
    else:
        return False

def triangle_class(a,b,c):
    if (is_valid(a,b,c)):
        if(a==b==c):
            return("Equilateral")
        elif((a==b)or(a==c)or(b==c)):
            return("Isoscales")
        elif((a**2)+(b**2)==(c**2) or (a**2)+(c**2)==(b**2) or (c**2)+(b**2)==(a**2)):
            return("RightAngle")
        else:
            return("Scalen ")
    else:
        return("Invalid Triangle")
def circumRadius(a,b,c):
    side=max(a,b,c)
    radius=(side/2)       
    if(is_valid(a,b,c)):
        if(triangle_class(a,b,c)=="RightAngle"):
           return radius;
        else:
            return -1
    else:
        print("Invalid")

def main():
    a,b,c=input("Enter the side  of the triangle with space").split(' ')
    a,b,c=int(a),int(b),int(c) 
    print(is_valid(a,b,c))
    print(triangle_class(a,b,c))
    print(circumRadius(a,b,c))
main()
