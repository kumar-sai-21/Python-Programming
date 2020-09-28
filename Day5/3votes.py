#3.
#SAI KUMAR SATAPATHY
x=input("Enter the list of tickets:")
lst=x.split()
c=[]
d={}
for i in lst:
    if i not in c:
        d[i]=0
        c.append(i)
    else:
        d[i]=int(d[i])+1
print("WINNER",max(d,key=d.get))