#given attributes(x,y,r) for two circles identify if the circles intersect,touch or not intersect

def circle(x1,y1,r1,x2,y2,r2):
    distSq=(((x1-x2)**2)+(y1-y2)**2)
    radSumSq=(r1+r2)**2
    if(distSq==radSumSq):
        return 1
    elif(distSq>radSumSq):
        return -1
    else:
        return 0
x1,y1,r1=input("enter coordinates and radius of 1st circle(seperated by space):").split()
x1,y1,r1=int(x1),int(y1),int(r1)
x2,y2,r2=input("enter coordinates and radius of 2nd circle(seperated by space):").split()
x2,y2,r2=int(x2),int(y2),int(r2)
c=circle(x1,y1,r1,x2,y2,r2)
if(c==1):
    print("circle touch each other")
elif(c==-1):
    print("circle not intersect to each other")
else:
    print("circle intersect to each other")
