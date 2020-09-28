#WAP TO FIND GCD OF TWO NUMBER
#SAI KUMAR SATAPATHY(190310248)
#GCD(GRATEST INTEGER DIGIT)


a=int(input("Enter the First no:"))
b=int(input("Enter the Second No:"))
if(a>b):
    small=b
else:
    small=a
for i in range(1,small+1):
    if((a%i==0)and(b%i==0)):
        gcd=i
print("The GCD is:",gcd)
