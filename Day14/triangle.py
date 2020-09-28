class triangle:
    def __init__(self,x,y,z):
        self.__x=x
        self.__y=y
        self.__z=z
    @property
    def x(self):
        return self.__x
    @property
    def y(self):
        return self.__y
    @property
    def z(self):
        return self.__z
    @z.setter
    def z(self,r):
        self.__z=z
    def area(self):
        s=0.5*(self.__x+self.__y+self.__z)
        return (s*(s-self.__x)*(s-self.__y)*(s-self.__z)**0.5)
    def perimeter (self):
        return self.__x+self.__y+self.__z
    def triangle_class (self):
        if (x==y==z) :
            return("Equilateral")
        elif ((x**2+y**2)==z**2 or (x**2+z**2)==y**2 or (z**2+y**2)==x**2):
            return("Right_angled")
        elif (x==y or y==z or z==x):
            return("Isoceles")
        else:
            return("Scalene")
    def circumRadius (self):
        if (self.triangle_class(x,y,z) =="Right_angled"):
            r=max(x,y,z)
            return(r/2)        
        else:
            return("-1")
x=int(input("Enter length of side 1"))
y=int(input("Enter length of side 2"))
z=int(input("Enter length of side 3"))
if not (x+y>z and x+z>y and y+z>x ):
    print("side cannot be negative")
    exit(0)
t1=triangle(x,y,z)
print("Side1={} , Side2={} , Side3={}".format(t1.x,t1.y,t1.z))
print("area=",t1.area())
print("perimeter",t1.perimeter())
print(t1.triangle_class())
if t1.triangle_class()=="Right_angled":
    print(t1.circumRadius())
