#wap to calulate the area of triangle
#for equalaterial triangle
x=int(input("Enter the side the triangle "))
area=x**3
print("Area ", area)
#for scalen and isoscles triangle

a=int(input("Enter the 1st side of triangel "))
b=int(input("Enter the 2nd side of triangel "))
c=int(input("Enter the 3rd side of triangel "))
p=(a+b+c)/2
print(p)
areas=(p*((p-a)*(p-b)*(p-c)))**0.5
print(areas)
