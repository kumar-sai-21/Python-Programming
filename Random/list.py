import random
l1=[]
l2=[]
for i in range(0,10):
    n=random.randint(0,30)
    l1.append(n)
print(l1)
for i in range(0,15):
    n=random.randint(30,50)
    l2.append(n)
print(l2)
#print(l1+l2)
print (set(l1+l2))
#print(len(l1+l2))