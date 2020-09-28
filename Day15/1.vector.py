#2. Design a vector class that will support some of the vector operations like:
    #− Add (+)
    #− Sub (-)
    #− Mul (*)
    #− ABS (abs)

import math
class Vector:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __repr__(self):
        return "vector({},{})".format(self.a,self.b)
    def __add__(self, other):
        x=self.a+other.a
        y=self.b+other.b
        return Vector(x,y)
    def __sub__(self, other):
        x=self.a-other.a
        y=self.b-other.b
        return Vector(x,y)
    def __mul__(self, other):
        x=self.a*other.a
        y=self.b*other.b
        return Vector(x,y)
    def __abs__(self):
        return math.hypot(self.x,self.y)

#v1=(input("Enter the first vector"))
#x,y=v1.split(" ")
v1=Vector(2,3)
#v2=(input("Enter the second vector"))
#x,y=v2.split(" ")
v2=Vector(3,2)
print(v1+v2)
print(v1-v2)
print(v1*v2)
print(abs(v1))


