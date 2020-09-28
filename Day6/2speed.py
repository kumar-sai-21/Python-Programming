#2. Accept two sequence of number, one for distance another for time and return a list of speeds
#SAI KUMAR SATAPATHY`
a=input("Enter distances separated by commas").split(",")
b=input("Enter time separated by commas").split(",")
c=[]
if(len(a)!=len(b)):
    print("Enter same no of values")
else:
    for i in range(len(a)):
        c.append(int(a[i])/int(b[i]))
    print(c)

