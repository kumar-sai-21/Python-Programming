import math
def tria(a,b,c): 
    a1 = (a**2) 
    b1 = (b**2) 
    c1 = (c** 2) 
  
    if (a1 == a1 + b1 or b1 == a1 + c1 or c1 == a1 + b1): 
        print("Right-angled Triangle") 
  
    elif(a1 > c1 + b1 or b1 > a1+ c1 or c1 > a1 + b1): 
        print("Obtuse-angled Triangle") 
  
    else: 
        print("Acute-angled Triangle")


a,b,c=input("Enter the side  of the triangle with space").split(' ')
a,b,c=int(a),int(b),int(c)
ra_a = (b**2+c**2-a**2)/(2.0*b*c)
ra_b = (a**2+c**2-b**2)/(2.0*a*c)

a_= math.degrees(math.acos(ra_a))
b_= math.degrees(math.acos(ra_b))

print(type(a_),type(b_))
c_= 180.0 -(a_+b_)

    #(((b**2)+(c**2))-(a**2))/(2*b*c))
#b= math.acos((((a**2)+(c**2))-(b**2))/(2*a*c));
#c= math.acos((((a**2)+(b**2))-(c**2))/(2*a*c));
print(a_)
print(b_)
print (c_)

#print(b)
#print(c)
tria(a,b,c)
