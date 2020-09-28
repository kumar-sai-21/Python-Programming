#2. Input a comma separated list from console. Write a program to print this list after
#removing all duplicate values with original order reserved
#SAI KUMAR SATAPATHY
n= input ("Enter no separated by comma ")
x= n.split(",")
res=[]
for i in x:
    if i not in res:
        res.append(i)
print(res)
res=' ' .join(reversed(res))
print(res)

