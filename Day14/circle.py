import sys
class circle:
    def __init__(self,x,y,r):
        self.x=x
        self.y=y
        try:
            assert r>0
        except:
            print("Radius cant be negative")
            sys.exit()
        self.r=r
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def r(self):
        return self.__r
    @x.setter
    def x(self,x):
        self.__x=x
    @y.setter
    def y(self, y):
        self.__y = y
    @r.setter
    def r(self,r):
        self.__r=r
    def area(self):
        return 3.14*self.__r*self.__r
    def perimeter (self):
        return 2*3.14*self.__r 
    def distcen(self):
        return ((self.__x*self.__x)+(self.__y*self.__y))**0.5
    def distcircum(self):
        return self.distcen ()-self.__r
x=int(input("Enter x coordinate"))
y=int(input("Enter y coordinate"))
r=int(input("Enter radius"))
c1=circle(x,y,r)
print("Xcoordinate={} , Ycoordinate={} , Radius={}".format(c1.x,c1.y,c1.r))
print(c1.area())
print(c1.perimeter())
print(c1.distcen())
print(c1.distcircum())
