

from array import *
a= array('i',[1,2,3,4,5,6])
print(a[0])
print(type(a))
print(len(a))
#ADDING ELEMENT
a.append(3) #add a single element at the end
print(a)
a.extend([44,65,76]) # add multiple element at the end
print(a)
a.insert(2,4444) #add particular element at a particular palce
print(a)
#DELETING ELEMENT
print(a.pop()) # return the value
print(a)
print(a.remove(44)) #does't return the value
print(a)

b= array('i',[11,22,33,44,45,26])
c= array('i')
c=a+b
print(c)
print(a[0:5])
print(a[0:-5])
for x in c[3:5]:
    print(x)
b=0
while(b<c[6]):
    print(b)
    b+=1
print ('new while')
while(b<len(a)):
    print(a[b])
    b=b+1