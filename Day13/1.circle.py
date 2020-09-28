#sai kumar satapathy
def circle(x1, y1, x2, y2, r1, r2): 
   
    dist = (x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2);  
    Sum = (r1 + r2) * (r1 + r2);  
    if (dist == Sum): 
        return 1 
    elif (dist > Sum): 
        return -1 
    else: 
        return 0 
   
   
x = (input("Enter the x coodinate"))
x1,x2=x.split(" ")
print(x1)
x1=int(x1)
print(x2)
x2=int(x2)
y = (input("Enter the y coodinate"))
y1,y2=y.split(" ")
print(y1)
y1=int(y1)
print(y2)
y2=int(y2)
r=(input("Enter the Radius"))
r1,r2=x.split(" ")
print(r1)
r1=int(r1)
print(r2)
r2=int(r2)
 
t = circle(x1, y1, x2, y2, r1, r2)  
if (t == 1): 
    print("Circle touched")  
elif (t < 0): 
    print("Circle do not touch")  
else: 
    print("Circle intersected")