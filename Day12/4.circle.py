import math
class circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        self.r=r
    def area(self):
        return 3.142*self.r*self.r
    def perimeter(self):
        return 3.142*2*self.r
    def dstorg(self):
        return math.sqrt(self.x**2+self.y**2)
    def crm_dst(self):
        return((math.sqrt(self.x**2+self.y**2))-self.r)
c1=circle(3,2,1)
print("Area of the circle is : ",c1.area())
print("Perimeter of the circle is : ",c1.perimeter())
print("Distance of center from origin is : ",c1.dstorg())
print("Distance og circumference from origin is : ",c1.crm_dst())
    
